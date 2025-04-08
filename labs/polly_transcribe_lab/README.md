# 🎙️ Amazon Polly + Amazon Transcribe Lab

Ce lab vous permet d'explorer deux services AWS de machine learning pré-entraînés : **Amazon Polly** (Text-to-Speech) et **Amazon Transcribe** (Speech-to-Text).

## 🔧 Objectif
1. Convertir un texte en audio avec Amazon Polly.
2. Stocker l'audio sur Amazon S3.
3. Transcrire l'audio en texte avec Amazon Transcribe.
4. Comparer le texte transcrit au texte initial.

## 📁 Fichiers

- `sample_text.txt` : texte à transformer en audio.
- `text_to_speech.py` : script de génération audio avec Polly.
- `upload_to_s3.py` : script pour uploader l'audio sur S3.
- `start_transcription.py` : lancement de la transcription.
- `check_transcription.py` : récupération du texte transcrit.

## ✅ Prérequis

- AWS CLI configuré (`aws configure`)
- Boto3 installé (`pip install boto3`)
- Bucket S3 existant

## 🚀 Utilisation

1. Modifier le nom du bucket dans `upload_to_s3.py` et `start_transcription.py`.
2. Exécuter les scripts dans cet ordre :

```bash
python text_to_speech.py
python upload_to_s3.py
python start_transcription.py
python check_transcription.py
