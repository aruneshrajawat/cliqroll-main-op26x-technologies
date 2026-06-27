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
        if len(audio) < 16000:
            print("Audio too short, skipping")
            return None
        wav = preprocess_wav(audio)
        embedding = encoder.embed_utterance(wav)
        return embedding.tolist()
    except Exception as e:
        print(f"Error in voice embedding: {e}")
        return None
    

def identify_speaker(new_embedding, candidate_dict, threshold=0.65, min_margin=0.05):
    if new_embedding is None or not candidate_dict:
        return None, 0.0
    new_emb = np.array(new_embedding)
    new_emb = new_emb / (np.linalg.norm(new_emb) + 1e-10)

    scores = []
    for sid, stored_embedding in candidate_dict.items():
        if stored_embedding:
            stored_emb = np.array(stored_embedding)
            stored_emb = stored_emb / (np.linalg.norm(stored_emb) + 1e-10)
            similarity = float(np.dot(new_emb, stored_emb))
            scores.append((sid, similarity))

    if not scores:
        return None, 0.0

    scores.sort(key=lambda x: x[1], reverse=True)
    best_sid, best_score = scores[0]
    second_score = scores[1][1] if len(scores) > 1 else -1

    if best_score >= threshold and (best_score - second_score) >= min_margin:
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
            if (end - start) < 16000:
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

