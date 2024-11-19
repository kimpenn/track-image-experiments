CREATE TABLE IF NOT EXISTS assay (
  id bigint PRIMARY KEY AUTO_INCREMENT,
  staining_date date DEFAULT NULL,
  imaging_date date DEFAULT NULL,
  imaging_by_id bigint UNIQUE,
  microscope_id bigint UNIQUE,
  staining_by_id bigint UNIQUE,
  staining_protocol_id bigint UNIQUE,
  name integer unsigned UNIQUE
);

CREATE UNIQUE INDEX core_assay_staining_protocol_id_66fdc63c ON assay (staining_protocol_id);
CREATE UNIQUE INDEX core_assay_staining_by_id_2084e9aa ON assay (staining_by_id);
CREATE UNIQUE INDEX core_assay_microscope_id_1aa9af50 ON assay (microscope_id);
CREATE UNIQUE INDEX core_assay_imaging_by_id_e3600e1f ON assay (imaging_by_id);
CREATE UNIQUE INDEX sqlite_autoindex_core_assay_1 ON assay (name);

CREATE TABLE IF NOT EXISTS assay_probe_panel (
  id integer PRIMARY KEY AUTO_INCREMENT,
  assay_id bigint UNIQUE,
  panel_id bigint UNIQUE
);

CREATE UNIQUE INDEX core_assay_probe_panel_panel_id_2fc52fd9 ON assay_probe_panel (panel_id);
CREATE UNIQUE INDEX core_assay_probe_panel_assay_id_70b603ba ON assay_probe_panel (assay_id);
CREATE UNIQUE INDEX core_assay_probe_panel_assay_id_panel_id_58ec64e0_uniq ON assay_probe_panel (assay_id, panel_id);

CREATE TABLE IF NOT EXISTS assay_slides_applied (
  id integer PRIMARY KEY AUTO_INCREMENT,
  assay_id bigint UNIQUE,
  slide_id bigint UNIQUE
);

CREATE UNIQUE INDEX core_assay_slides_applied_slide_id_71311bfe ON assay_slides_applied (slide_id);
CREATE UNIQUE INDEX core_assay_slides_applied_assay_id_db4308f5 ON assay_slides_applied (assay_id);
CREATE UNIQUE INDEX core_assay_slides_applied_assay_id_slide_id_a702b204_uniq ON assay_slides_applied (assay_id, slide_id);

CREATE TABLE IF NOT EXISTS exposuretime (
  id integer PRIMARY KEY AUTO_INCREMENT,
  probe_id bigint UNIQUE,
  microscope_id bigint UNIQUE,
  exposure_time decimal
);

CREATE UNIQUE INDEX core_exposuretime_microscope_id_d1cd6ad0 ON exposuretime (microscope_id);
CREATE UNIQUE INDEX core_exposuretime_probe_id_d3d7ba0a ON exposuretime (probe_id);

CREATE TABLE IF NOT EXISTS microscope (
  id bigint PRIMARY KEY AUTO_INCREMENT,
  model varchar(500),
  name varchar(500) UNIQUE,
  json_description varchar(500)
);

CREATE UNIQUE INDEX sqlite_autoindex_core_microscope_1 ON microscope (name);

CREATE TABLE IF NOT EXISTS panel (
  id bigint PRIMARY KEY AUTO_INCREMENT,
  description varchar(500),
  notes text,
  name varchar(500) UNIQUE
);

CREATE UNIQUE INDEX sqlite_autoindex_core_panel_1 ON panel (name);

CREATE TABLE IF NOT EXISTS probe (
  id bigint PRIMARY KEY AUTO_INCREMENT,
  target_analyte varchar(500),
  target_gencode_id varchar(500),
  antibody_clone_id varchar(500),
  imaging_notes text,
  staining_notes text,
  stock_concentration varchar(500),
  working_dilution varchar(500),
  probe_type_id bigint UNIQUE,
  name varchar(500) UNIQUE,
  fish_technology_id bigint UNIQUE,
  fluorescent_molecule_id bigint UNIQUE,
  imaging_success_id bigint UNIQUE
);

CREATE UNIQUE INDEX core_probe_imaging_success_id_d230edcb ON probe (imaging_success_id);
CREATE UNIQUE INDEX core_probe_fluorescent_molecule_id_b2bf1d58 ON probe (fluorescent_molecule_id);
CREATE UNIQUE INDEX core_probe_fish_technology_id_a013e9c0 ON probe (fish_technology_id);
CREATE UNIQUE INDEX core_probe_probe_type_id_80852e3c ON probe (probe_type_id);
CREATE UNIQUE INDEX sqlite_autoindex_core_probe_1 ON probe (name);

CREATE TABLE IF NOT EXISTS probe_probe_panel (
  id integer PRIMARY KEY AUTO_INCREMENT,
  probe_id bigint UNIQUE,
  panel_id bigint UNIQUE
);

CREATE UNIQUE INDEX core_probe_probe_panel_panel_id_ab23712c ON probe_probe_panel (panel_id);
CREATE UNIQUE INDEX core_probe_probe_panel_probe_id_57cb0257 ON probe_probe_panel (probe_id);
CREATE UNIQUE INDEX core_probe_probe_panel_probe_id_panel_id_795aa5ca_uniq ON probe_probe_panel (probe_id, panel_id);

CREATE TABLE IF NOT EXISTS sliceorculture (
  id integer PRIMARY KEY AUTO_INCREMENT,
  name varchar(500) UNIQUE,
  type varchar(500),
  storage_time integer,
  prep_date date DEFAULT NULL,
  acquired_from_id bigint UNIQUE,
  organ_id bigint UNIQUE,
  organ_region_id bigint UNIQUE,
  parent_id bigint UNIQUE,
  prep_by_id bigint UNIQUE,
  slide_id bigint UNIQUE,
  treatment_id bigint UNIQUE
);

CREATE UNIQUE INDEX core_sliceorculture_treatment_id_b1f33b8d ON sliceorculture (treatment_id);
CREATE UNIQUE INDEX core_sliceorculture_slide_id_b0228d05 ON sliceorculture (slide_id);
CREATE UNIQUE INDEX core_sliceorculture_prep_by_id_14ec56ec ON sliceorculture (prep_by_id);
CREATE UNIQUE INDEX core_sliceorculture_parent_id_46c41273 ON sliceorculture (parent_id);
CREATE UNIQUE INDEX core_sliceorculture_organ_region_id_ce6d8bde ON sliceorculture (organ_region_id);
CREATE UNIQUE INDEX core_sliceorculture_organ_id_92da1082 ON sliceorculture (organ_id);
CREATE UNIQUE INDEX core_sliceorculture_acquired_from_id_066d60b4 ON sliceorculture (acquired_from_id);
CREATE UNIQUE INDEX sqlite_autoindex_core_sliceorculture_1 ON sliceorculture (name);

CREATE TABLE IF NOT EXISTS slide (
  id bigint PRIMARY KEY AUTO_INCREMENT,
  name varchar(500) UNIQUE
);

CREATE UNIQUE INDEX sqlite_autoindex_core_slide_1 ON slide (name);

CREATE TABLE IF NOT EXISTS source (
  id bigint PRIMARY KEY AUTO_INCREMENT,
  lab_id varchar(500) UNIQUE,
  public_id varchar(500),
  public_id_source varchar(500),
  sex varchar(500),
  age smallint unsigned,
  species_id bigint UNIQUE
);

CREATE UNIQUE INDEX core_source_species_id_77c9f7d8 ON source (species_id);
CREATE UNIQUE INDEX sqlite_autoindex_core_source_1 ON source (lab_id);

ALTER TABLE assay ADD CONSTRAINT fk_core_assay_microscope_id_core_microscope_id FOREIGN KEY (microscope_id) REFERENCES microscope (id);
ALTER TABLE assay_probe_panel ADD CONSTRAINT fk_core_assay_probe_panel_assay_id_core_assay_id FOREIGN KEY (assay_id) REFERENCES assay (id);
ALTER TABLE assay_probe_panel ADD CONSTRAINT fk_core_assay_probe_panel_panel_id_core_panel_id FOREIGN KEY (panel_id) REFERENCES panel (id);
ALTER TABLE assay_slides_applied ADD CONSTRAINT fk_core_assay_slides_applied_assay_id_core_assay_id FOREIGN KEY (assay_id) REFERENCES assay (id);
ALTER TABLE assay_slides_applied ADD CONSTRAINT fk_core_assay_slides_applied_slide_id_core_slide_id FOREIGN KEY (slide_id) REFERENCES slide (id);
ALTER TABLE exposuretime ADD CONSTRAINT fk_core_exposuretime_microscope_id_core_microscope_id FOREIGN KEY (microscope_id) REFERENCES microscope (id);
ALTER TABLE exposuretime ADD CONSTRAINT fk_core_exposuretime_probe_id_core_probe_id FOREIGN KEY (probe_id) REFERENCES probe (id);
ALTER TABLE probe_probe_panel ADD CONSTRAINT fk_core_probe_probe_panel_panel_id_core_panel_id FOREIGN KEY (panel_id) REFERENCES panel (id);
ALTER TABLE probe_probe_panel ADD CONSTRAINT fk_core_probe_probe_panel_probe_id_core_probe_id FOREIGN KEY (probe_id) REFERENCES probe (id);
ALTER TABLE sliceorculture ADD CONSTRAINT fk_core_sliceorculture_parent_id_core_source_id FOREIGN KEY (parent_id) REFERENCES source (id);
ALTER TABLE sliceorculture ADD CONSTRAINT fk_core_sliceorculture_slide_id_core_slide_id FOREIGN KEY (slide_id) REFERENCES slide (id);

