# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.0.0] - 2024-06-13

### Added
- Criação do extrator de dados para a api externa rickandmortyapi
- Adicionado prefect tasks e flows
- Adicionado comando para executar o extrator juntamente com o prefect

### Fixed
- Correções na views de Character, Episode e Location

## [1.0.2] - 2024-06-12

### Fixed
- Corrigidos campos url de Episode e Location para unique
- Correção na views de Episode e Location de acordo com a mudança

## [1.0.1] - 2024-06-12

### Fixed
- Corrigidos campos de Episode e Location para many to many 
- Correção no README.md e requirements.txt

## [1.0.0] - 2024-06-12

### Added
- Configuração inicial do Django
- Criação do Banco de Dados
- Criação de models, serializers, views e urls para Episode, Location e Character
- Criação do README com detalhes de instalação e execução