%global sounds_dir %{_datadir}/asterisk/sounds
%global en_AU_version 1.6.1
%global en_GB_version 1.6.1
%global en_version 1.6.1
%global es_version 1.6.1
%global fr_version 1.6.1
%global it_version 1.6.1
%global ja_version 1.6.1
%global ru_version 1.6.1
%global sv_version 1.6.1

Name:           asterisk-sounds-core
Version:        1.6.1
Release:        19%{?dist}
Summary:        Core sounds for Asterisk


# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
URL:            http://www.asterisk.org/

Source0:        http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-alaw-%{en_version}.tar.gz
Source1:        http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-g722-%{en_version}.tar.gz
Source2:        http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-g729-%{en_version}.tar.gz
Source3:        http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-gsm-%{en_version}.tar.gz
Source4:        http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-siren7-%{en_version}.tar.gz
Source5:        http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-siren14-%{en_version}.tar.gz
Source6:        http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-sln16-%{en_version}.tar.gz
Source7:        http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-ulaw-%{en_version}.tar.gz
Source8:        http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en-wav-%{en_version}.tar.gz

Source10:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-alaw-%{es_version}.tar.gz
Source11:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-g722-%{es_version}.tar.gz
Source12:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-g729-%{es_version}.tar.gz
Source13:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-gsm-%{es_version}.tar.gz
Source14:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-siren7-%{es_version}.tar.gz
Source15:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-siren14-%{es_version}.tar.gz
Source16:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-sln16-%{es_version}.tar.gz
Source17:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-ulaw-%{es_version}.tar.gz
Source18:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-es-wav-%{es_version}.tar.gz

Source20:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-alaw-%{fr_version}.tar.gz
Source21:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-g722-%{fr_version}.tar.gz
Source22:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-g729-%{fr_version}.tar.gz
Source23:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-gsm-%{fr_version}.tar.gz
Source24:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-siren7-%{fr_version}.tar.gz
Source25:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-siren14-%{fr_version}.tar.gz
Source26:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-sln16-%{fr_version}.tar.gz
Source27:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-ulaw-%{fr_version}.tar.gz
Source28:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-wav-%{fr_version}.tar.gz

Source30:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_AU-alaw-%{en_AU_version}.tar.gz
Source31:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_AU-g722-%{en_AU_version}.tar.gz
Source32:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_AU-g729-%{en_AU_version}.tar.gz
Source33:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_AU-gsm-%{en_AU_version}.tar.gz
Source34:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_AU-siren7-%{en_AU_version}.tar.gz
Source35:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_AU-siren14-%{en_AU_version}.tar.gz
Source36:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_AU-sln16-%{en_AU_version}.tar.gz
Source37:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_AU-ulaw-%{en_AU_version}.tar.gz
Source38:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_AU-wav-%{en_AU_version}.tar.gz

Source40:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ru-alaw-%{ru_version}.tar.gz
Source41:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ru-g722-%{ru_version}.tar.gz
Source42:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ru-g729-%{ru_version}.tar.gz
Source43:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ru-gsm-%{ru_version}.tar.gz
Source44:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ru-siren7-%{ru_version}.tar.gz
Source45:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ru-siren14-%{ru_version}.tar.gz
Source46:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ru-sln16-%{ru_version}.tar.gz
Source47:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ru-ulaw-%{ru_version}.tar.gz
Source48:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ru-wav-%{ru_version}.tar.gz

Source50:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-it-alaw-%{it_version}.tar.gz
Source51:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-it-g722-%{it_version}.tar.gz
Source52:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-it-g729-%{it_version}.tar.gz
Source53:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-it-gsm-%{it_version}.tar.gz
Source54:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-it-siren7-%{it_version}.tar.gz
Source55:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-it-siren14-%{it_version}.tar.gz
Source56:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-it-sln16-%{it_version}.tar.gz
Source57:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-it-ulaw-%{it_version}.tar.gz
Source58:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-it-wav-%{it_version}.tar.gz

Source60:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_GB-alaw-%{en_GB_version}.tar.gz
Source61:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_GB-g722-%{en_GB_version}.tar.gz
Source62:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_GB-g729-%{en_GB_version}.tar.gz
Source63:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_GB-gsm-%{en_GB_version}.tar.gz
Source64:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_GB-siren7-%{en_GB_version}.tar.gz
Source65:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_GB-siren14-%{en_GB_version}.tar.gz
Source66:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_GB-sln16-%{en_GB_version}.tar.gz
Source67:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_GB-ulaw-%{en_GB_version}.tar.gz
Source68:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-en_GB-wav-%{en_GB_version}.tar.gz

Source70:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ja-alaw-%{ja_version}.tar.gz
Source71:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ja-g722-%{ja_version}.tar.gz
Source72:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ja-g729-%{ja_version}.tar.gz
Source73:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ja-gsm-%{ja_version}.tar.gz
Source74:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ja-siren7-%{ja_version}.tar.gz
Source75:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ja-siren14-%{ja_version}.tar.gz
Source76:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ja-sln16-%{ja_version}.tar.gz
Source77:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ja-ulaw-%{ja_version}.tar.gz
Source78:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-ja-wav-%{ja_version}.tar.gz

Source80:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-sv-alaw-%{sv_version}.tar.gz
Source81:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-sv-g722-%{sv_version}.tar.gz
Source82:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-sv-g729-%{sv_version}.tar.gz
Source83:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-sv-gsm-%{sv_version}.tar.gz
Source84:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-sv-siren7-%{sv_version}.tar.gz
Source85:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-sv-siren14-%{sv_version}.tar.gz
Source86:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-sv-sln16-%{sv_version}.tar.gz
Source87:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-sv-ulaw-%{sv_version}.tar.gz
Source88:       http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-sv-wav-%{sv_version}.tar.gz

BuildArch:      noarch

%description
Core sound files for Asterisk.

%package en
Summary: Core English sound files for Asterisk
Requires: asterisk >= 1.4.0

%description en
Core English sound files for Asterisk.

%package en-alaw
Summary: Core English ALAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en-alaw
Core English ALAW sound files for Asterisk.

%package en-g722
Summary: Core English G.722 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en-g722
Core English G.722 sound files for Asterisk.

%package en-g729
Summary: Core English G.729 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en-g729
Core English G.729 sound files for Asterisk.

%package en-gsm
Summary: Core English GSM sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en-gsm
Core English GSM sound files for Asterisk.

%package en-siren7
Summary: Core English Siren7 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en-siren7
Core English Siren7 sound files for Asterisk.

%package en-siren14
Summary: Core English GSM sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en-siren14
Core English Siren14 sound files for Asterisk.

%package en-sln16
Summary: Core English SLN16 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en-sln16
Core English SLN16 sound files for Asterisk.

%package en-ulaw
Summary: Core English ULAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en-ulaw
Core English ULAW sound files for Asterisk.

%package en-wav
Summary: Core English WAV sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en-wav
Core English WAV sound files for Asterisk.

%package es
Summary: Core Spanish sound files for Asterisk
Requires: asterisk >= 1.4.0

%description es
Core Spanish sound files for Asterisk.

%package es-alaw
Summary: Core Spanish ALAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-es = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description es-alaw
Core Spanish ALAW sound files for Asterisk.

%package es-g722
Summary: Core Spanish G.722 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-es = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description es-g722
Core Spanish G.722 sound files for Asterisk.

%package es-g729
Summary: Core Spanish G.729 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-es = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description es-g729
Core Spanish G.729 sound files for Asterisk.

%package es-gsm
Summary: Core Spanish GSM sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-es = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description es-gsm
Core Spanish GSM sound files for Asterisk.

%package es-siren7
Summary: Core Spanish Siren7 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-es = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description es-siren7
Core Spanish Siren7 sound files for Asterisk.

%package es-siren14
Summary: Core Spanish Siren14 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-es = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description es-siren14
Core Spanish Siren14 sound files for Asterisk.

%package es-sln16
Summary: Core Spanish SLN16 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-es = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description es-sln16
Core Spanish SLN16 sound files for Asterisk.

%package es-ulaw
Summary: Core Spanish ULAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-es = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description es-ulaw
Core Spanish ULAW sound files for Asterisk.

%package es-wav
Summary: Core Spanish WAV sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-es = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description es-wav
Core Spanish WAV sound files for Asterisk.

%package fr
Summary: Core French sound files for Asterisk
Requires: asterisk >= 1.4.0

%description fr
Core French sound files for Asterisk.

%package fr-alaw
Summary: Core French ALAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-fr = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description fr-alaw
Core French ALAW sound files for Asterisk.

%package fr-g722
Summary: Core French G.722 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-fr = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description fr-g722
Core French G.722 sound files for Asterisk.

%package fr-g729
Summary: Core French G.729 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-fr = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description fr-g729
Core French G.729 sound files for Asterisk.

%package fr-gsm
Summary: Core French GSM sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-fr = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description fr-gsm
Core French GSM sound files for Asterisk.

%package fr-siren7
Summary: Core French Siren7 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-fr = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description fr-siren7
Core French Siren7 sound files for Asterisk.

%package fr-siren14
Summary: Core French Siren14 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-fr = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description fr-siren14
Core French Siren14 sound files for Asterisk.

%package fr-sln16
Summary: Core French SLN16 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-fr = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description fr-sln16
Core French SLN16 sound files for Asterisk.

%package fr-ulaw
Summary: Core French ULAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-fr = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description fr-ulaw
Core French ULAW sound files for Asterisk.

%package fr-wav
Summary: Core French WAV sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-fr = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description fr-wav
Core French WAV sound files for Asterisk.

%package en_AU
Summary: Core English (Australian) sound files for Asterisk
Requires: asterisk >= 1.4.0

%description en_AU
Core English (Australian) sound files for Asterisk.

%package en_AU-alaw
Summary: Core English (Australian) ALAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_AU = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_AU-alaw
Core English (Australian) ALAW sound files for Asterisk.

%package en_AU-g722
Summary: Core English (Australian) G.722 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_AU = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_AU-g722
Core English (Australian) G.722 sound files for Asterisk.

%package en_AU-g729
Summary: Core English (Australian) G.729 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_AU = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_AU-g729
Core English (Australian) G.729 sound files for Asterisk.

%package en_AU-gsm
Summary: Core English (Australian) GSM sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_AU = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_AU-gsm
Core English (Australian) GSM sound files for Asterisk.

%package en_AU-siren7
Summary: Core English (Australian) Siren7 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_AU = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_AU-siren7
Core English (Australian) Siren7 sound files for Asterisk.

%package en_AU-siren14
Summary: Core English (Australian) Siren14 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_AU = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_AU-siren14
Core English (Australian) Siren14 sound files for Asterisk.

%package en_AU-sln16
Summary: Core English (Australian) SLN16 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_AU = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_AU-sln16
Core English (Australian) SLN16 sound files for Asterisk.

%package en_AU-ulaw
Summary: Core English (Australian) ULAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_AU = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_AU-ulaw
Core English (Australian) ULAW sound files for Asterisk.

%package en_AU-wav
Summary: Core English (Australian) WAV sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_AU = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_AU-wav
Core English (Australian) WAV sound files for Asterisk.

%package ru
Summary: Core Russian sound files for Asterisk
Requires: asterisk >= 1.4.0

%description ru
Core Russian sound files for Asterisk.

%package ru-alaw
Summary: Core Russian ALAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ru = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ru-alaw
Core Russian ALAW sound files for Asterisk.

%package ru-g722
Summary: Core Russian G.722 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ru = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ru-g722
Core Russian G.722 sound files for Asterisk.

%package ru-g729
Summary: Core Russian G.729 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ru = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ru-g729
Core Russian G.729 sound files for Asterisk.

%package ru-gsm
Summary: Core Russian GSM sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ru = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ru-gsm
Core Russian GSM sound files for Asterisk.

%package ru-siren7
Summary: Core Russian Siren7 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ru = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ru-siren7
Core Russian Siren7 sound files for Asterisk.

%package ru-siren14
Summary: Core Russian Siren14 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ru = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ru-siren14
Core Russian Siren14 sound files for Asterisk.

%package ru-sln16
Summary: Core Russian SLN16 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ru = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ru-sln16
Core Russian SLN16 sound files for Asterisk.

%package ru-ulaw
Summary: Core Russian ULAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ru = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ru-ulaw
Core Russian ULAW sound files for Asterisk.

%package ru-wav
Summary: Core Russian WAV sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ru = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ru-wav
Core Russian WAV sound files for Asterisk.

%package it
Summary: Core Italian sound files for Asterisk
Requires: asterisk >= 1.4.0

%description it
Core Italian sound files for Asterisk.

%package it-alaw
Summary: Core Italian ALAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-it = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description it-alaw
Core Italian ALAW sound files for Asterisk.

%package it-g722
Summary: Core Italian G.722 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-it = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description it-g722
Core Italian G.722 sound files for Asterisk.

%package it-g729
Summary: Core Italian G.729 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-it = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description it-g729
Core Italian G.729 sound files for Asterisk.

%package it-gsm
Summary: Core Italian GSM sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-it = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description it-gsm
Core Italian GSM sound files for Asterisk.

%package it-siren7
Summary: Core Italian Siren7 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-it = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description it-siren7
Core Italian Siren7 sound files for Asterisk.

%package it-siren14
Summary: Core Italian Siren14 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-it = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description it-siren14
Core Italian Siren14 sound files for Asterisk.

%package it-sln16
Summary: Core Italian SLN16 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-it = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description it-sln16
Core Italian SLN16 sound files for Asterisk.

%package it-ulaw
Summary: Core Italian ULAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-it = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description it-ulaw
Core Italian ULAW sound files for Asterisk.

%package it-wav
Summary: Core Italian WAV sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-it = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description it-wav
Core Italian WAV sound files for Asterisk.

%package en_GB
Summary: Core English (United Kingdom) sound files for Asterisk
Requires: asterisk >= 1.4.0

%description en_GB
Core English (United Kingdom) sound files for Asterisk.

%package en_GB-alaw
Summary: Core English (United Kingdom) ALAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_GB = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_GB-alaw
Core English (United Kingdom) ALAW sound files for Asterisk.

%package en_GB-g722
Summary: Core English (United Kingdom) G.722 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_GB = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_GB-g722
Core English (United Kingdom) G.722 sound files for Asterisk.

%package en_GB-g729
Summary: Core English (United Kingdom) G.729 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_GB = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_GB-g729
Core English (United Kingdom) G.729 sound files for Asterisk.

%package en_GB-gsm
Summary: Core English (United Kingdom) GSM sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_GB = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_GB-gsm
Core English (United Kingdom) GSM sound files for Asterisk.

%package en_GB-siren7
Summary: Core English (United Kingdom) Siren7 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_GB = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_GB-siren7
Core English (United Kingdom) Siren7 sound files for Asterisk.

%package en_GB-siren14
Summary: Core English (United Kingdom) Siren14 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_GB = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_GB-siren14
Core English (United Kingdom) Siren14 sound files for Asterisk.

%package en_GB-sln16
Summary: Core English (United Kingdom) SLN16 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_GB = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_GB-sln16
Core English (United Kingdom) SLN16 sound files for Asterisk.

%package en_GB-ulaw
Summary: Core English (United Kingdom) ULAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_GB = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_GB-ulaw
Core English (United Kingdom) ULAW sound files for Asterisk.

%package en_GB-wav
Summary: Core English (United Kingdom) WAV sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-en_GB = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description en_GB-wav
Core English (United Kingdom) WAV sound files for Asterisk.

%package ja
Summary: Core Japanese sound files for Asterisk
Requires: asterisk >= 1.4.0

%description ja
Core Japanese sound files for Asterisk.

%package ja-alaw
Summary: Core Japanese ALAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ja = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ja-alaw
Core Japanese ALAW sound files for Asterisk.

%package ja-g722
Summary: Core Japanese G.722 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ja = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ja-g722
Core Japanese G.722 sound files for Asterisk.

%package ja-g729
Summary: Core Japanese G.729 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ja = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ja-g729
Core Japanese G.729 sound files for Asterisk.

%package ja-gsm
Summary: Core Japanese GSM sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ja = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ja-gsm
Core Japanese GSM sound files for Asterisk.

%package ja-siren7
Summary: Core Japanese Siren7 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ja = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ja-siren7
Core Japanese Siren7 sound files for Asterisk.

%package ja-siren14
Summary: Core Japanese Siren14 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ja = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ja-siren14
Core Japanese Siren14 sound files for Asterisk.

%package ja-sln16
Summary: Core Japanese SLN16 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ja = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ja-sln16
Core Japanese SLN16 sound files for Asterisk.

%package ja-ulaw
Summary: Core Japanese ULAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ja = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ja-ulaw
Core Japanese ULAW sound files for Asterisk.

%package ja-wav
Summary: Core Japanese WAV sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-ja = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description ja-wav
Core Japanese WAV sound files for Asterisk.

%package sv
Summary: Core Swedish sound files for Asterisk
Requires: asterisk >= 1.4.0

%description sv
Core Swedish sound files for Asterisk.

%package sv-alaw
Summary: Core Swedish ALAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-sv = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description sv-alaw
Core Swedish ALAW sound files for Asterisk.

%package sv-g722
Summary: Core Swedish G.722 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-sv = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description sv-g722
Core Swedish G.722 sound files for Asterisk.

%package sv-g729
Summary: Core Swedish G.729 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-sv = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description sv-g729
Core Swedish G.729 sound files for Asterisk.

%package sv-gsm
Summary: Core Swedish GSM sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-sv = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description sv-gsm
Core Swedish GSM sound files for Asterisk.

%package sv-siren7
Summary: Core Swedish Siren7 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-sv = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description sv-siren7
Core Swedish Siren7 sound files for Asterisk.

%package sv-siren14
Summary: Core Swedish Siren14 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-sv = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description sv-siren14
Core Swedish Siren14 sound files for Asterisk.

%package sv-sln16
Summary: Core Swedish SLN16 sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-sv = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description sv-sln16
Core Swedish SLN16 sound files for Asterisk.

%package sv-ulaw
Summary: Core Swedish ULAW sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-sv = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description sv-ulaw
Core Swedish ULAW sound files for Asterisk.

%package sv-wav
Summary: Core Swedish WAV sound files for Asterisk
Requires: asterisk >= 1.4.0
Requires: asterisk-sounds-core-sv = %{version}-%{release}
Provides: asterisk-sounds-core = %{version}-%{release}

%description sv-wav
Core Swedish WAV sound files for Asterisk.

%prep

%setup -c -T 

%build

for file in %{S:0} %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{S:6} %{S:7} %{S:8}
do
  tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/!' > `basename $file .tar.gz`.list
  tar --extract --directory . --file $file
done

mkdir es

for file in %{S:10} %{S:11} %{S:12} %{S:13} %{S:14} %{S:15} %{S:16} %{S:17} %{S:18}
do
  tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/es/!' > `basename $file .tar.gz`.list
  tar --extract --directory ./es/ --file $file
done

mkdir fr

for file in %{S:20} %{S:21} %{S:22} %{S:23} %{S:24} %{S:25} %{S:26} %{S:27} %{S:28}
do
  tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/fr/!' > `basename $file .tar.gz`.list
  tar --extract --directory ./fr/  --file $file
done

iconv -f iso-8859-1 -t utf-8 < fr/core-sounds-fr.txt > fr/core-sounds-fr.txt.tmp
touch --reference fr/core-sounds-fr.txt fr/core-sounds-fr.txt.tmp
mv fr/core-sounds-fr.txt.tmp fr/core-sounds-fr.txt

mkdir en_AU

for file in %{S:30} %{S:31} %{S:32} %{S:33} %{S:34} %{S:35} %{S:36} %{S:37} %{S:38}
do
  tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/en_AU/!' > `basename $file .tar.gz`.list
  tar --extract --directory ./en_AU/  --file $file
done

mkdir ru

for file in %{S:40} %{S:41} %{S:42} %{S:43} %{S:44} %{S:45} %{S:46} %{S:47} %{S:48}
do
  tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/ru/!' > `basename $file .tar.gz`.list
  tar --extract --directory ./ru/  --file $file
done

mkdir it

for file in %{S:50} %{S:51} %{S:52} %{S:53} %{S:54} %{S:55} %{S:56} %{S:57} %{S:58}
do
  tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/it/!' > `basename $file .tar.gz`.list
  tar --extract --directory ./it/  --file $file
done

mkdir en_GB

for file in %{S:60} %{S:61} %{S:62} %{S:63} %{S:64} %{S:65} %{S:66} %{S:67} %{S:68}
do
  tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/en_GB/!' > `basename $file .tar.gz`.list
  tar --extract --directory ./en_GB/  --file $file
done

mkdir ja

for file in %{S:70} %{S:71} %{S:72} %{S:73} %{S:74} %{S:75} %{S:76} %{S:77} %{S:78}
do
  tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/ja/!' > `basename $file .tar.gz`.list
  tar --extract --directory ./ja/  --file $file
done

mkdir sv

for file in %{S:80} %{S:81} %{S:82} %{S:83} %{S:84} %{S:85} %{S:86} %{S:87} %{S:88}
do
  tar --list --file $file | grep -E '.(alaw|g722|g729|gsm|siren7|siren14|sln16|ulaw|wav)$' | sed -e 's!^!%{sounds_dir}/sv/!' > `basename $file .tar.gz`.list
  tar --extract --directory ./sv/  --file $file
done

%install
rm -rf %{buildroot}

for file in `cat *.list | sed -e 's!^%{sounds_dir}/!!'`
do
  mkdir -p %{buildroot}%{sounds_dir}/`dirname $file`
  cp -p $file %{buildroot}%{sounds_dir}/$file
done

%files en
%doc core-sounds-en.txt
%doc CHANGES-asterisk-core-en-%{en_version}
%doc CREDITS-asterisk-core-en-%{en_version}
%license LICENSE-asterisk-core-en-%{en_version}
%dir %{sounds_dir}/dictate/
%dir %{sounds_dir}/digits/
%dir %{sounds_dir}/followme/
%dir %{sounds_dir}/letters/
%dir %{sounds_dir}/phonetic/

%files en-alaw -f asterisk-core-sounds-en-alaw-%{en_version}.list
%doc asterisk-core-sounds-en-alaw-%{en_version}.list

%files en-g722 -f asterisk-core-sounds-en-g722-%{en_version}.list
%doc asterisk-core-sounds-en-g722-%{en_version}.list

%files en-g729 -f asterisk-core-sounds-en-g729-%{en_version}.list
%doc asterisk-core-sounds-en-g729-%{en_version}.list

%files en-gsm -f asterisk-core-sounds-en-gsm-%{en_version}.list
%doc asterisk-core-sounds-en-gsm-%{en_version}.list

%files en-siren7 -f asterisk-core-sounds-en-siren7-%{en_version}.list
%doc asterisk-core-sounds-en-siren7-%{en_version}.list

%files en-siren14 -f asterisk-core-sounds-en-siren14-%{en_version}.list
%doc asterisk-core-sounds-en-gsm-%{en_version}.list

%files en-sln16 -f asterisk-core-sounds-en-sln16-%{en_version}.list
%doc asterisk-core-sounds-en-sln16-%{en_version}.list

%files en-ulaw -f asterisk-core-sounds-en-ulaw-%{en_version}.list
%doc asterisk-core-sounds-en-ulaw-%{en_version}.list

%files en-wav -f asterisk-core-sounds-en-wav-%{en_version}.list
%doc asterisk-core-sounds-en-wav-%{en_version}.list

%files es
%doc es/core-sounds-es.txt
%doc es/CHANGES-asterisk-core-es-%{es_version}
%doc es/CREDITS-asterisk-core-es-%{es_version}
%license es/LICENSE-asterisk-core-es-%{es_version}
%dir %{sounds_dir}/es/
%dir %{sounds_dir}/es/dictate/
%dir %{sounds_dir}/es/digits/
%dir %{sounds_dir}/es/followme/
%dir %{sounds_dir}/es/letters/
%dir %{sounds_dir}/es/phonetic/

%files es-alaw -f asterisk-core-sounds-es-alaw-%{es_version}.list
%doc asterisk-core-sounds-es-alaw-%{es_version}.list

%files es-g722 -f asterisk-core-sounds-es-g722-%{es_version}.list
%doc asterisk-core-sounds-es-g722-%{es_version}.list

%files es-g729 -f asterisk-core-sounds-es-g729-%{es_version}.list
%doc asterisk-core-sounds-es-g729-%{es_version}.list

%files es-gsm -f asterisk-core-sounds-es-gsm-%{es_version}.list
%doc asterisk-core-sounds-es-gsm-%{es_version}.list

%files es-siren7 -f asterisk-core-sounds-es-siren7-%{es_version}.list
%doc asterisk-core-sounds-es-siren7-%{es_version}.list

%files es-siren14 -f asterisk-core-sounds-es-siren14-%{es_version}.list
%doc asterisk-core-sounds-es-siren14-%{es_version}.list

%files es-sln16 -f asterisk-core-sounds-es-sln16-%{es_version}.list
%doc asterisk-core-sounds-es-sln16-%{es_version}.list

%files es-ulaw -f asterisk-core-sounds-es-ulaw-%{es_version}.list
%doc asterisk-core-sounds-es-ulaw-%{es_version}.list

%files es-wav -f asterisk-core-sounds-es-wav-%{es_version}.list
%doc asterisk-core-sounds-es-wav-%{es_version}.list

%files fr
%doc fr/core-sounds-fr.txt
%doc fr/CHANGES-asterisk-core-fr-%{fr_version}
%doc fr/CREDITS-asterisk-core-fr-%{fr_version}
%license fr/LICENSE-asterisk-core-fr-%{fr_version}
%dir %{sounds_dir}/fr/
%dir %{sounds_dir}/fr/dictate/
%dir %{sounds_dir}/fr/digits/
%dir %{sounds_dir}/fr/followme/
%dir %{sounds_dir}/fr/letters/
%dir %{sounds_dir}/fr/phonetic/

%files fr-alaw -f asterisk-core-sounds-fr-alaw-%{fr_version}.list
%doc asterisk-core-sounds-fr-alaw-%{fr_version}.list

%files fr-g722 -f asterisk-core-sounds-fr-g722-%{fr_version}.list
%doc asterisk-core-sounds-fr-g722-%{fr_version}.list

%files fr-g729 -f asterisk-core-sounds-fr-g729-%{fr_version}.list
%doc asterisk-core-sounds-fr-g729-%{fr_version}.list

%files fr-gsm -f asterisk-core-sounds-fr-gsm-%{fr_version}.list
%doc asterisk-core-sounds-fr-gsm-%{fr_version}.list

%files fr-siren7 -f asterisk-core-sounds-fr-siren7-%{fr_version}.list
%doc asterisk-core-sounds-fr-siren7-%{fr_version}.list

%files fr-siren14 -f asterisk-core-sounds-fr-siren14-%{fr_version}.list
%doc asterisk-core-sounds-fr-siren14-%{fr_version}.list

%files fr-sln16 -f asterisk-core-sounds-fr-sln16-%{fr_version}.list
%doc asterisk-core-sounds-fr-sln16-%{fr_version}.list

%files fr-ulaw -f asterisk-core-sounds-fr-ulaw-%{fr_version}.list
%doc asterisk-core-sounds-fr-ulaw-%{fr_version}.list

%files fr-wav -f asterisk-core-sounds-fr-wav-%{fr_version}.list
%doc asterisk-core-sounds-fr-wav-%{fr_version}.list

%files en_AU
%doc en_AU/core-sounds-en_AU.txt
%doc en_AU/CHANGES-asterisk-core-en_AU-%{en_AU_version}
%doc en_AU/CREDITS-asterisk-core-en_AU-%{en_AU_version}
%license en_AU/LICENSE-asterisk-core-en_AU-%{en_AU_version}
%dir %{sounds_dir}/en_AU/
%dir %{sounds_dir}/en_AU/dictate/
%dir %{sounds_dir}/en_AU/digits/
%dir %{sounds_dir}/en_AU/followme/
%dir %{sounds_dir}/en_AU/letters/
%dir %{sounds_dir}/en_AU/phonetic/

%files en_AU-alaw -f asterisk-core-sounds-en_AU-alaw-%{en_AU_version}.list
%doc asterisk-core-sounds-en_AU-alaw-%{en_AU_version}.list

%files en_AU-g722 -f asterisk-core-sounds-en_AU-g722-%{en_AU_version}.list
%doc asterisk-core-sounds-en_AU-g722-%{en_AU_version}.list

%files en_AU-g729 -f asterisk-core-sounds-en_AU-g729-%{en_AU_version}.list
%doc asterisk-core-sounds-en_AU-g729-%{en_AU_version}.list

%files en_AU-gsm -f asterisk-core-sounds-en_AU-gsm-%{en_AU_version}.list
%doc asterisk-core-sounds-en_AU-gsm-%{en_AU_version}.list

%files en_AU-siren7 -f asterisk-core-sounds-en_AU-siren7-%{en_AU_version}.list
%doc asterisk-core-sounds-en_AU-siren7-%{en_AU_version}.list

%files en_AU-siren14 -f asterisk-core-sounds-en_AU-siren14-%{en_AU_version}.list
%doc asterisk-core-sounds-en_AU-siren14-%{en_AU_version}.list

%files en_AU-sln16 -f asterisk-core-sounds-en_AU-sln16-%{en_AU_version}.list
%doc asterisk-core-sounds-en_AU-sln16-%{en_AU_version}.list

%files en_AU-ulaw -f asterisk-core-sounds-en_AU-ulaw-%{en_AU_version}.list
%doc asterisk-core-sounds-en_AU-ulaw-%{en_AU_version}.list

%files en_AU-wav -f asterisk-core-sounds-en_AU-wav-%{en_AU_version}.list
%doc asterisk-core-sounds-en_AU-wav-%{en_AU_version}.list

%files ru
%doc ru/core-sounds-ru.txt
%doc ru/CHANGES-asterisk-core-ru-%{ru_version}
%doc ru/CREDITS-asterisk-core-ru-%{ru_version}
%license ru/LICENSE-asterisk-core-ru-%{ru_version}
%dir %{sounds_dir}/ru/
%dir %{sounds_dir}/ru/dictate/
%dir %{sounds_dir}/ru/digits/
%dir %{sounds_dir}/ru/followme/
%dir %{sounds_dir}/ru/letters/
%dir %{sounds_dir}/ru/phonetic/

%files ru-alaw -f asterisk-core-sounds-ru-alaw-%{ru_version}.list
%doc asterisk-core-sounds-ru-alaw-%{ru_version}.list

%files ru-g722 -f asterisk-core-sounds-ru-g722-%{ru_version}.list
%doc asterisk-core-sounds-ru-g722-%{ru_version}.list

%files ru-g729 -f asterisk-core-sounds-ru-g729-%{ru_version}.list
%doc asterisk-core-sounds-ru-g729-%{ru_version}.list

%files ru-gsm -f asterisk-core-sounds-ru-gsm-%{ru_version}.list
%doc asterisk-core-sounds-ru-gsm-%{ru_version}.list

%files ru-siren7 -f asterisk-core-sounds-ru-siren7-%{ru_version}.list
%doc asterisk-core-sounds-ru-siren7-%{ru_version}.list

%files ru-siren14 -f asterisk-core-sounds-ru-siren14-%{ru_version}.list
%doc asterisk-core-sounds-ru-siren14-%{ru_version}.list

%files ru-sln16 -f asterisk-core-sounds-ru-sln16-%{ru_version}.list
%doc asterisk-core-sounds-ru-sln16-%{ru_version}.list

%files ru-ulaw -f asterisk-core-sounds-ru-ulaw-%{ru_version}.list
%doc asterisk-core-sounds-ru-ulaw-%{ru_version}.list

%files ru-wav -f asterisk-core-sounds-ru-wav-%{ru_version}.list
%doc asterisk-core-sounds-ru-wav-%{ru_version}.list

%files it
%doc it/core-sounds-it.txt
%doc it/CHANGES-asterisk-core-it-%{it_version}
%doc it/CREDITS-asterisk-core-it-%{it_version}
%license it/LICENSE-asterisk-core-it-%{it_version}
%dir %{sounds_dir}/it/
%dir %{sounds_dir}/it/dictate/
%dir %{sounds_dir}/it/digits/
%dir %{sounds_dir}/it/followme/
%dir %{sounds_dir}/it/letters/
%dir %{sounds_dir}/it/phonetic/

%files it-alaw -f asterisk-core-sounds-it-alaw-%{it_version}.list
%doc asterisk-core-sounds-it-alaw-%{it_version}.list

%files it-g722 -f asterisk-core-sounds-it-g722-%{it_version}.list
%doc asterisk-core-sounds-it-g722-%{it_version}.list

%files it-g729 -f asterisk-core-sounds-it-g729-%{it_version}.list
%doc asterisk-core-sounds-it-g729-%{it_version}.list

%files it-gsm -f asterisk-core-sounds-it-gsm-%{it_version}.list
%doc asterisk-core-sounds-it-gsm-%{it_version}.list

%files it-siren7 -f asterisk-core-sounds-it-siren7-%{it_version}.list
%doc asterisk-core-sounds-it-siren7-%{it_version}.list

%files it-siren14 -f asterisk-core-sounds-it-siren14-%{it_version}.list
%doc asterisk-core-sounds-it-siren14-%{it_version}.list

%files it-sln16 -f asterisk-core-sounds-it-sln16-%{it_version}.list
%doc asterisk-core-sounds-it-sln16-%{it_version}.list

%files it-ulaw -f asterisk-core-sounds-it-ulaw-%{it_version}.list
%doc asterisk-core-sounds-it-ulaw-%{it_version}.list

%files it-wav -f asterisk-core-sounds-it-wav-%{it_version}.list
%doc asterisk-core-sounds-it-wav-%{it_version}.list

%files en_GB
%doc en_GB/core-sounds-en_GB.txt
%doc en_GB/CHANGES-asterisk-core-en_GB-%{en_GB_version}
%doc en_GB/CREDITS-asterisk-core-en_GB-%{en_GB_version}
%license en_GB/LICENSE-asterisk-core-en_GB-%{en_GB_version}
%dir %{sounds_dir}/en_GB/
%dir %{sounds_dir}/en_GB/dictate/
%dir %{sounds_dir}/en_GB/digits/
%dir %{sounds_dir}/en_GB/followme/
%dir %{sounds_dir}/en_GB/letters/
%dir %{sounds_dir}/en_GB/phonetic/

%files en_GB-alaw -f asterisk-core-sounds-en_GB-alaw-%{en_GB_version}.list
%doc asterisk-core-sounds-en_GB-alaw-%{en_GB_version}.list

%files en_GB-g722 -f asterisk-core-sounds-en_GB-g722-%{en_GB_version}.list
%doc asterisk-core-sounds-en_GB-g722-%{en_GB_version}.list

%files en_GB-g729 -f asterisk-core-sounds-en_GB-g729-%{en_GB_version}.list
%doc asterisk-core-sounds-en_GB-g729-%{en_GB_version}.list

%files en_GB-gsm -f asterisk-core-sounds-en_GB-gsm-%{en_GB_version}.list
%doc asterisk-core-sounds-en_GB-gsm-%{en_GB_version}.list

%files en_GB-siren7 -f asterisk-core-sounds-en_GB-siren7-%{en_GB_version}.list
%doc asterisk-core-sounds-en_GB-siren7-%{en_GB_version}.list

%files en_GB-siren14 -f asterisk-core-sounds-en_GB-siren14-%{en_GB_version}.list
%doc asterisk-core-sounds-en_GB-siren14-%{en_GB_version}.list

%files en_GB-sln16 -f asterisk-core-sounds-en_GB-sln16-%{en_GB_version}.list
%doc asterisk-core-sounds-en_GB-sln16-%{en_GB_version}.list

%files en_GB-ulaw -f asterisk-core-sounds-en_GB-ulaw-%{en_GB_version}.list
%doc asterisk-core-sounds-en_GB-ulaw-%{en_GB_version}.list

%files en_GB-wav -f asterisk-core-sounds-en_GB-wav-%{en_GB_version}.list
%doc asterisk-core-sounds-en_GB-wav-%{en_GB_version}.list

%files ja
%doc ja/core-sounds-ja.txt
%doc ja/CHANGES-asterisk-core-ja-%{ja_version}
%doc ja/CREDITS-asterisk-core-ja-%{ja_version}
%license ja/LICENSE-asterisk-core-ja-%{ja_version}
%dir %{sounds_dir}/ja/
%dir %{sounds_dir}/ja/dictate/
%dir %{sounds_dir}/ja/digits/
%dir %{sounds_dir}/ja/followme/
%dir %{sounds_dir}/ja/letters/
%dir %{sounds_dir}/ja/phonetic/

%files ja-alaw -f asterisk-core-sounds-ja-alaw-%{ja_version}.list
%doc asterisk-core-sounds-ja-alaw-%{ja_version}.list

%files ja-g722 -f asterisk-core-sounds-ja-g722-%{ja_version}.list
%doc asterisk-core-sounds-ja-g722-%{ja_version}.list

%files ja-g729 -f asterisk-core-sounds-ja-g729-%{ja_version}.list
%doc asterisk-core-sounds-ja-g729-%{ja_version}.list

%files ja-gsm -f asterisk-core-sounds-ja-gsm-%{ja_version}.list
%doc asterisk-core-sounds-ja-gsm-%{ja_version}.list

%files ja-siren7 -f asterisk-core-sounds-ja-siren7-%{ja_version}.list
%doc asterisk-core-sounds-ja-siren7-%{ja_version}.list

%files ja-siren14 -f asterisk-core-sounds-ja-siren14-%{ja_version}.list
%doc asterisk-core-sounds-ja-siren14-%{ja_version}.list

%files ja-sln16 -f asterisk-core-sounds-ja-sln16-%{ja_version}.list
%doc asterisk-core-sounds-ja-sln16-%{ja_version}.list

%files ja-ulaw -f asterisk-core-sounds-ja-ulaw-%{ja_version}.list
%doc asterisk-core-sounds-ja-ulaw-%{ja_version}.list

%files ja-wav -f asterisk-core-sounds-ja-wav-%{ja_version}.list
%doc asterisk-core-sounds-ja-wav-%{ja_version}.list

%files sv
%doc sv/core-sounds-sv.txt
%doc sv/CHANGES-asterisk-core-sv-%{sv_version}
%doc sv/CREDITS-asterisk-core-sv-%{sv_version}
%license sv/LICENSE-asterisk-core-sv-%{sv_version}
%dir %{sounds_dir}/sv/
%dir %{sounds_dir}/sv/dictate/
%dir %{sounds_dir}/sv/digits/
%dir %{sounds_dir}/sv/followme/
%dir %{sounds_dir}/sv/letters/
%dir %{sounds_dir}/sv/phonetic/

%files sv-alaw -f asterisk-core-sounds-sv-alaw-%{sv_version}.list
%doc asterisk-core-sounds-sv-alaw-%{sv_version}.list

%files sv-g722 -f asterisk-core-sounds-sv-g722-%{sv_version}.list
%doc asterisk-core-sounds-sv-g722-%{sv_version}.list

%files sv-g729 -f asterisk-core-sounds-sv-g729-%{sv_version}.list
%doc asterisk-core-sounds-sv-g729-%{sv_version}.list

%files sv-gsm -f asterisk-core-sounds-sv-gsm-%{sv_version}.list
%doc asterisk-core-sounds-sv-gsm-%{sv_version}.list

%files sv-siren7 -f asterisk-core-sounds-sv-siren7-%{sv_version}.list
%doc asterisk-core-sounds-sv-siren7-%{sv_version}.list

%files sv-siren14 -f asterisk-core-sounds-sv-siren14-%{sv_version}.list
%doc asterisk-core-sounds-sv-siren14-%{sv_version}.list

%files sv-sln16 -f asterisk-core-sounds-sv-sln16-%{sv_version}.list
%doc asterisk-core-sounds-sv-sln16-%{sv_version}.list

%files sv-ulaw -f asterisk-core-sounds-sv-ulaw-%{sv_version}.list
%doc asterisk-core-sounds-sv-ulaw-%{sv_version}.list

%files sv-wav -f asterisk-core-sounds-sv-wav-%{sv_version}.list
%doc asterisk-core-sounds-sv-wav-%{sv_version}.list

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.1-18
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Jared Smith <jsmith@fedoraproject.org> - 1.6.1-2
- Update to upstream 1.6.1 release for ASTERISK-16172 bug

* Fri Nov 24 2017 Jared Smith <jsmith@fedoraproject.org> - 1.6-1
- Update to upstream 1.6 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Jared Smith <jsmith@fedoraproject.org> - 1.5.0-1
- Update to version 1.5
- Add Swedish language files
- Remove calls to %%defattr macro, as they are no longer needed

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 27 2014 Jeffrey Ollie <jeff@ocjtech.us> - 1.4.26-1
- Added ja sounds.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar  6 2014 Jeffrey Ollie <jeff@ocjtech.us> - 1.4.25-1
- Added en_GB sounds

* Wed Aug 21 2013 Jeffrey Ollie <jeff@ocjtech.us> - 1.4.24-1
- Add Italian (it) sounds
- Fix BZ999376 fix summary for asterisk-sounds-core-ru

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 28 2013 Jeffrey Ollie <jeff@ocjtech.us> - 1.4.23-1
- Update to 1.4.23

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 12 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.22-1
- Update to 1.4.22
- Add some macros to allow different languages to be at different versions

* Tue Jun 28 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.21-1
- Add Russian (ru) sounds

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 18 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.20-1
- Update to 1.4.20
- Add en_AU sounds

* Tue Aug  3 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.19-1
- Update to 1.4.19

* Fri Dec  4 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16-3
- Add fr/1.g729 back and build with new version of RPM.

* Mon Nov  2 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16-2
- Remove fr/1.g729 as it's triggering an error in magic_file(3) (BZ#532489)

* Mon Oct  5 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16-1
- Update to 1.4.16.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr  8 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-1
- Update to new release of sounds.
- Add sounds encoded with siren7 and siren14.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.14-1
- Add dist tag back in.

* Fri Jan 30 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.14-1
- First version for Fedora
