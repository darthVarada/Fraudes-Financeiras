// src/components/Presentation.jsx
// Este componente exibe uma apresentação de slides interativa
import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import arquiteturaImg from '../assets/arquitetura-projeto-times.jpeg'; // Imagem da arquitetura

// Definição dos slides: título, subtítulo, descrição e configurações visuais
const slides = [
  {
    title: 'SecureTrust',
    subtitle: 'Engenharia de Dados para Detecção de Fraudes Financeiras',
    description:
      'Fraudes financeiras podem ocorrer em segundos. Nosso desafio: detectar padrões fraudulentos antes que causem prejuízo.',
    bgClass: 'bg-gradient-to-br from-black via-gray-900 to-gray-800',
  },
  {
    title: 'O Problema',
    subtitle: 'Fraudes em Transações Digitais',
    description:
      'Perdas financeiras recorrentes, segurança comprometida e resposta lenta. Era preciso agir com dados e inteligência.',
    bgClass: 'bg-gradient-to-br from-red-900 via-black to-gray-900',
  },
  {
    title: 'Objetivo do Projeto',
    subtitle: 'Solução Preditiva com Governança',
    description:
      'Criar pipeline de ingestão, tratamento, exposição e visualização de dados com foco em ML e BI.',
    bgClass: 'bg-gradient-to-br from-purple-900 via-black to-gray-800',
  },
  {
    title: 'Arquitetura do Pipeline',
    subtitle: 'Camadas Bronze, Silver, Gold',
    description:
      'Visão geral das camadas de dados: RAW no S3, tratamento no Glue e consultas via Athena.',
    image: arquiteturaImg,
    bgClass: 'bg-gradient-to-br from-blue-900 via-black to-gray-900',
  },
  {
    title: 'Detalhes Técnicos',
    subtitle: 'Bronze → Silver → Gold → Analytics',
    description:
      'Bronze (RAW): CSV no S3. Silver (REF): Glue limpa e enriquece. Gold: Athena serve dados para notebooks e dashboards.',
    bgClass: 'bg-gradient-to-br from-green-900 via-black to-gray-800',
  },
  {
    title: 'Transformações no Glue',
    subtitle: 'Tratamento Automatizado',
    description:
      'Substituição de -1 por NaN, remoção de duplicatas, exclusão de coluna irrelevante e criação de month_named.',
    bgClass: 'bg-gradient-to-br from-indigo-900 via-black to-gray-800',
  },
  {
    title: 'Governança & Segurança',
    subtitle: 'Compliance e Rastreabilidade',
    description:
      'Dados sintéticos anonimizados, IAM no S3/Athena, LGPD simulada e catálogo de metadados.',
    bgClass: 'bg-gradient-to-br from-gray-900 via-black to-yellow-900',
  },
  {
    title: 'Qualidade dos Dados',
    subtitle: 'Confiança Analítica',
    description:
      'Validações de tipagem e integridade, relatório de qualidade via Python e preparo para modelagem.',
    bgClass: 'bg-gradient-to-br from-teal-900 via-black to-gray-800',
  },
  {
    title: 'Análise Exploratória',
    subtitle: 'Padrões e Outliers',
    description:
      'Histogramas, correlações, sazonalidade e identificação de variáveis chave para ML.',
    bgClass: 'bg-gradient-to-br from-pink-900 via-black to-gray-900',
  },
  {
    title: 'Modelagem com XGBoost',
    subtitle: 'Machine Learning Supervisionado',
    description:
      'Recall: 92%, AUC ROC: 0.97, Falsos Positivos: 5% (meta <3%) e precisão de 89%.',
    bgClass: 'bg-gradient-to-br from-yellow-900 via-black to-gray-800',
  },
  {
    title: 'Resultados & Métricas',
    subtitle: 'Impacto Real',
    description:
      'Pipeline validado, dados prontos para BI, redução de falsos positivos e insights em tempo real.',
    bgClass: 'bg-gradient-to-br from-blue-700 via-black to-gray-800',
  },
  {
    title: 'Dashboards Interativos',
    subtitle: 'Power BI e Visualizações',
    description:
      'KPIs dinâmicos, heatmaps, filtros por canal, dispositivo, região e perfil de cliente.',
    bgClass: 'bg-gradient-to-br from-red-700 via-black to-gray-900',
  },
  {
    title: 'Monitoramento & Ciclo de Vida',
    subtitle: 'Logs e Retenção',
    description:
      'Políticas de retenção (RAW 3m, PRATA 12m), logs no Glue/Athena e revisão semestral.',
    bgClass: 'bg-gradient-to-br from-green-700 via-black to-gray-900',
  },
  {
    title: 'Conclusão',
    subtitle: 'Prontos para Escalar',
    description:
      'Pipeline robusto, governado e escalável. Próximos passos: nuvem, imputação e dashboards automáticos.',
    bgClass: 'bg-gradient-to-br from-gray-800 via-black to-indigo-800',
  },
  {
    title: 'Próximos Passos & Agradecimentos',
    subtitle: 'Obrigado!',
    description:
      'Dúvidas? Entre em contato: Davi Sasso, Rodrigo Alex, Victor Barradas.',
    bgClass: 'bg-gradient-to-br from-purple-800 via-black to-gray-900',
  },
];

export default function Presentation() {
  // Indice do slide atual
  const [currentSlide, setCurrentSlide] = useState(0);

  // Navegação: próximo e anterior
  const next = () => setCurrentSlide((i) => (i + 1) % slides.length);
  const prev = () => setCurrentSlide((i) => (i - 1 + slides.length) % slides.length);

  return (
    <div className={`min-h-screen flex items-center justify-center p-6 ${slides[currentSlide].bgClass}`}>
      <AnimatePresence exitBeforeEnter>
        <motion.div
          key={currentSlide}
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -30 }}
          transition={{ duration: 0.6 }}
          className="max-w-2xl text-center text-white"
        >
          <h1 className="text-4xl font-extrabold mb-2">{slides[currentSlide].title}</h1>
          <h2 className="text-xl font-semibold mb-4 text-purple-300">{slides[currentSlide].subtitle}</h2>
          <p className="mb-6 leading-relaxed">{slides[currentSlide].description}</p>
          {/* Renderiza imagem apenas se existir */}
          {slides[currentSlide].image && (
            <img
              src={slides[currentSlide].image}
              alt="Arquitetura do Projeto"
              className="mx-auto mb-6 rounded-lg shadow-lg max-h-72"
            />
          )}
          {/* Botões de navegação */}
          <div className="flex justify-center space-x-4">
            <button
              onClick={prev}
              className="px-5 py-2 border-2 border-white rounded-full hover:bg-white hover:text-black transition"
            >
              Anterior
            </button>
            <button
              onClick={next}
              className="px-5 py-2 border-2 border-white rounded-full hover:bg-white hover:text-black transition"
            >
              Próximo
            </button>
          </div>
        </motion.div>
      </AnimatePresence>
    </div>
  );
}


// src/App.jsx
// Componente raiz que importa e exibe a apresentação
import React from 'react';
import Presentation from './components/Presentation';

function App() {
  return <Presentation />;
}

export default App;


// tailwind.config.js
// Configuração básica para ativar o modo JIT e paths
module.exports = {
  mode: 'jit',
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false,
  theme: {
    extend: {},
  },
  variants: {},
  plugins: [],
};


// src/index.css
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Personalizações adicionais podem ser adicionadas aqui */


// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
