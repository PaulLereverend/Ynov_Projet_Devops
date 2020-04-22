-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le :  mar. 21 avr. 2020 à 17:29
-- Version du serveur :  10.3.22-MariaDB-0+deb10u1
-- Version de PHP :  7.3.11-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `ynov_devops`
--

-- --------------------------------------------------------

--
-- Structure de la table `data`
--

CREATE TABLE `data` (
  `id` int(11) NOT NULL,
  `unite_id` int(11) DEFAULT NULL,
  `automate_id` int(11) DEFAULT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `type` bigint(20) DEFAULT NULL,
  `date_prise` timestamp NOT NULL DEFAULT current_timestamp(),
  `temp_cuve` float DEFAULT 99.99,
  `temp_ext` float DEFAULT 99.99,
  `poids_lait` float DEFAULT 10000000,
  `mesure_ph` float DEFAULT 9999.9,
  `mesure_kplus` int(11) DEFAULT 65535,
  `mesure_nacl` float DEFAULT 9999.9,
  `salmonelle` int(11) DEFAULT 65535,
  `ecoli` int(11) DEFAULT 65535,
  `listeria` int(11) DEFAULT 65535
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `data`
--
-- --------------------------------------------------------

--
-- Structure de la table `site`
--

CREATE TABLE `site` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `site`
--

INSERT INTO `site` (`id`, `nom`) VALUES
(1, 'site1');

-- --------------------------------------------------------

--
-- Structure de la table `unite`
--

CREATE TABLE `unite` (
  `id` int(11) NOT NULL,
  `site_id` int(11) DEFAULT NULL,
  `nom` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `unite`
--

-- Index pour les tables déchargées
--

--
-- Index pour la table `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`id`),
  ADD KEY `unite_id` (`unite_id`);

--
-- Index pour la table `site`
--
ALTER TABLE `site`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `unite`
--
ALTER TABLE `unite`
  ADD PRIMARY KEY (`id`),
  ADD KEY `site_id` (`site_id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `data`
--
ALTER TABLE `data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1386;

--
-- AUTO_INCREMENT pour la table `site`
--
ALTER TABLE `site`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `unite`
--
ALTER TABLE `unite`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `data`
--
ALTER TABLE `data`
  ADD CONSTRAINT `data_ibfk_1` FOREIGN KEY (`unite_id`) REFERENCES `unite` (`id`);

--
-- Contraintes pour la table `unite`
--
ALTER TABLE `unite`
  ADD CONSTRAINT `unite_ibfk_1` FOREIGN KEY (`site_id`) REFERENCES `site` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
