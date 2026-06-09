from resemblyzer import VoiceEncoder,preprocess_wav
import numpy as np
import streamlit as st
import io
import librosa

@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()

def get_voice_embeddings(audio_bytes):
    try:
        encoder = load_voice_encoder()
        audio,sr = librosa.load(io.BytesIO(audio_bytes),sr = 16000)
        wav = preprocess_wav(audio)
        embedding = encoder.embed_utterance(wav)
        return embedding.tolist()
    except Exception as e:
        print(f"Error in voice embedding: {e}")
        return None
    

def identify_speaker(new_embedding, candidate_dict, threshold=0.65):
    if new_embedding is None or not candidate_dict:
        return None, 0.0
    best_sid = None
    best_score = -1

    new_emb = np.array(new_embedding)
    new_emb = new_emb / (np.linalg.norm(new_emb) + 1e-10)

    for sid, stored_embedding in candidate_dict.items():
        if stored_embedding:
            stored_emb = np.array(stored_embedding)
            stored_emb = stored_emb / (np.linalg.norm(stored_emb) + 1e-10)
            similarity = float(np.dot(new_emb, stored_emb))
            if similarity > best_score and similarity > threshold:
                best_score = similarity
                best_sid = sid
    if best_score >= threshold:
        return best_sid, best_score
    return None, best_score
            

def process_bulk_audio(audio_bytes,candidates_dic,threshold = 0.65):
    try:
        encoder = load_voice_encoder()
        audio,sr = librosa.load(io.BytesIO(audio_bytes),sr = 16000)
        segments = librosa.effects.split(audio,top_db = 30)


        identified_results = {}
        for start, end in segments:
            start, end = int(start), int(end)
            if (end - start) < 8000:
                continue 
            segment_audio = audio[start:end]
            wav = preprocess_wav(segment_audio)

            embedding = encoder.embed_utterance(wav)
            
            sid,score = identify_speaker(embedding,candidates_dic,threshold)
            
            if sid:
                if sid not in identified_results or score > identified_results[sid]:
                    identified_results[sid] = score
        return identified_results
    except Exception as e:
        print(f"Error in processing bulk audio: {e}")
        return {}

