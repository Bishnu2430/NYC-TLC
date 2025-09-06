# NYC TLC Big Data Analytics with Hadoop & Spark

A comprehensive big data project analyzing NYC Taxi & Limousine Commission (TLC) trip data using Apache Hadoop and Apache Spark on Ubuntu.

## 🚀 Project Overview

This project demonstrates:
- Large-scale data processing using Hadoop HDFS
- Real-time analytics with Apache Spark
- Distributed computing on taxi trip data
- Performance optimization techniques
- Data visualization and insights

## 🏗️ Architecture

NYC TLC Data Pipeline
Raw Parquet → HDFS → Spark Processing → Analytics & Visualization

## 📊 Dataset

- **Source**: NYC TLC Trip Record Data (2025)
- **Format**: Apache Parquet
- **Size**: ~10+ million records per month
- **Features**: Trip duration, distance, fares, locations, congestion pricing

## 🛠️ Tech Stack

- **Storage**: Hadoop HDFS 3.3.6
- **Processing**: Apache Spark 3.5.6
- **Resource Management**: YARN
- **Language**: Python (PySpark)
- **Visualization**: Matplotlib, Seaborn
- **Environment**: Ubuntu 22.04

## 📁 Repository Structure

nyc-tlc-big-data-project/
├── scripts/              # Analysis and processing scripts
├── config/               # Hadoop/Spark configuration files
├── docs/                 # Documentation and guides
├── notebooks/            # Jupyter notebooks
├── data-samples/         # Small sample datasets
├── results/              # Analysis outputs and visualizations
└── README.md
