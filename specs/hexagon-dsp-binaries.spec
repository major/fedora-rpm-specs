# Payload is Hexagon (QDSP6) ELF executed on the DSP via FastRPC, not host code
# skip dependency generation to avoid bogus soname Provides/Requires
%global __requires_exclude_from ^%{_datadir}/hexagon-dsp/.*
%global __provides_exclude_from ^%{_datadir}/hexagon-dsp/.*
# binutils strip does not understand Hexagon ELF and may corrupt the binaries
%global __strip %{_bindir}/true
# no debuginfo can be extracted from Hexagon ELF objects
%global debug_package %{nil}

Name:		hexagon-dsp-binaries
Version:	20261019
Release:	%autorelease
Summary:	Hexagon DSP binaries for FastRPC

License:	LicenseRef-Fedora-Firmware
URL:		https://github.com/linux-msm/hexagon-dsp-binaries
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc

ExclusiveArch:	%{arm64}

BuildArch:	noarch

BuildRequires:	make

%description
These packages provide binaries like FastRPC shell, C++ runtime, compressed
audio decoder modules and other libs for several Qualcomm platforms.

While qcom-firmware contains firmware for the DSPs present on the devices
using Qualcomm SoCs, using the FastRPC interfaces, compressed audio support
or getting the sensors data on those devices requires additional set of
binaries to be executed on the DSP side.

%define boardpkg() \
%package -n hexagon-dsp-binaries-%{1} \
Summary:	Hexagon DSP binaries for %{2} \
Requires:	hexagon-dsp-binaries = %{version}-%{release} \
Requires:	qcom-firmware \
%{?3:Requires:	hexagon-dsp-binaries-%{3} = %{version}-%{release}} \
%{?4:Requires:	hexagon-dsp-binaries-%{4} = %{version}-%{release}} \
%description -n hexagon-dsp-binaries-%{1} \
Hexagon DSP binaries and configuration for %{2}. \
%{?3:Uses DSP binaries from hexagon-dsp-binaries-%{3}%{?4: and hexagon-dsp-binaries-%{4}}.}

# Board list and inter-board linkage follow upstream config.txt
# Install: own DSP payload, Link: symlink into another board's tree
# Standalone boards (Install only)
%boardpkg qualcomm-db820c %{quote:Qualcomm Dragonboard 820c}
%boardpkg qualcomm-eliza-mtp %{quote:Qualcomm Eliza MTP}
%boardpkg qualcomm-glymur-crd %{quote:Qualcomm Glymur CRD}
%boardpkg qualcomm-hawi-mtp %{quote:Qualcomm Hawi MTP}
%boardpkg qualcomm-kaanapali-mtp %{quote:Qualcomm Kaanapali MTP}
%boardpkg qualcomm-sa8797p-ride-embedded %{quote:Qualcomm SA8797P Ride Embedded}
%boardpkg thundercomm-rb1 %{quote:Thundercomm RB1}
%boardpkg thundercomm-rb3gen2 %{quote:Thundercomm RB3 Gen 2}
%boardpkg qualcomm-qcs615-ride %{quote:Qualcomm QCS615 Ride}
%boardpkg radxa-dragon-q6a %{quote:Radxa Dragon Q6A}
%boardpkg thundercomm-rb2 %{quote:Thundercomm RB2}
%boardpkg qualcomm-sa8775p-ride %{quote:Qualcomm SA8775P Ride}
%boardpkg thundercomm-db845c %{quote:Thundercomm DB845c}
%boardpkg qualcomm-shikra-cqs-evk %{quote:Qualcomm Shikra CQS EVK}
%boardpkg thundercomm-rb5 %{quote:Thundercomm RB5}
%boardpkg qualcomm-sm8750-mtp %{quote:Qualcomm SM8750 MTP}
%boardpkg qualcomm-hamoa-iot-evk %{quote:Qualcomm Hamoa IoT EVK}
# Hybrid boards (adsp, cdsp or gdsp linked)
%boardpkg qualcomm-maili-mtp %{quote:Qualcomm Maili MTP} qualcomm-hawi-mtp
%boardpkg thundercomm-rubikpi3 %{quote:Thundercomm Rubik Pi 3} thundercomm-rb3gen2
%boardpkg qualcomm-qcs8300-ride %{quote:Qualcomm QCS8300 Ride} qualcomm-sa8775p-ride
# Linked boards (Link only)
%boardpkg qualcomm-eliza-cqs-evk %{quote:Qualcomm Eliza CQS EVK} qualcomm-eliza-mtp
%boardpkg qualcomm-mahua-crd %{quote:Qualcomm Mahua CRD} qualcomm-glymur-crd
%boardpkg arduino-imola %{quote:Arduino Imola} thundercomm-rb1
%boardpkg qualcomm-qcm6490-idp %{quote:Qualcomm QCM6490 IDP} thundercomm-rb3gen2
%boardpkg arduino-monza %{quote:Arduino Monza} qualcomm-qcs8300-ride qualcomm-sa8775p-ride
%boardpkg qualcomm-iq8275-evk %{quote:Qualcomm IQ8275 EVK} qualcomm-qcs8300-ride qualcomm-sa8775p-ride
%boardpkg qualcomm-monaco-draco-evk %{quote:Qualcomm Monaco Draco EVK} qualcomm-qcs8300-ride qualcomm-sa8775p-ride
%boardpkg qualcomm-iq9075-evk %{quote:Qualcomm IQ9075 EVK} qualcomm-sa8775p-ride
%boardpkg qualcomm-lemans-draco-evk %{quote:Qualcomm Lemans Draco EVK} qualcomm-sa8775p-ride
%boardpkg qualcomm-sdm845-hdk %{quote:Qualcomm SDM845 HDK} thundercomm-db845c
%boardpkg qualcomm-shikra-cqm-evk %{quote:Qualcomm Shikra CQM EVK} qualcomm-shikra-cqs-evk
%boardpkg qualcomm-shikra-iqs-evk %{quote:Qualcomm Shikra IQS EVK} qualcomm-shikra-cqs-evk
%boardpkg qualcomm-purwa-iot-evk %{quote:Qualcomm Purwa IoT EVK} qualcomm-hamoa-iot-evk
# Config only
%boardpkg qualcomm-db410c %{quote:Qualcomm DragonBoard 410c}

%prep
%autosetup

# don't install schema, it's mostly for development
sed -i '/schema.json/d' Makefile

%build
# Nothing to compile

%install
%make_install DSPDIR=%{_datadir}/hexagon-dsp

%files
%license LICENSE.qcom LICENSE.qcom-2 WHENCE LICENSE.MIT
%doc README.md
%dir %{_datadir}/hexagon-dsp
%dir %{_datadir}/hexagon-dsp/conf.d

%define boardfiles() \
%files -n hexagon-dsp-binaries-%{1} \
%{_datadir}/hexagon-dsp/conf.d/hexagon-dsp-binaries-%{1}.yaml \
%{?2:%dir %{_datadir}/hexagon-dsp/%{2}} \
%{?2:%dir %{_datadir}/hexagon-dsp/%{2}/%{3}} \
%{?2:%{_datadir}/hexagon-dsp/%{2}/%{3}/%{4}}

%boardfiles qualcomm-db820c apq8096 Qualcomm db820c
%boardfiles qualcomm-eliza-cqs-evk eliza Qualcomm Eliza-CQS-EVK
%boardfiles qualcomm-eliza-mtp eliza Qualcomm Eliza-MTP
%boardfiles qualcomm-glymur-crd glymur Qualcomm Glymur-CRD
%boardfiles qualcomm-hawi-mtp hawi Qualcomm Hawi-MTP
%boardfiles qualcomm-kaanapali-mtp kaanapali Qualcomm Kaanapali-MTP
%boardfiles qualcomm-mahua-crd mahua Qualcomm Mahua-CRD
%boardfiles qualcomm-maili-mtp maili Qualcomm Maili-MTP
%boardfiles qualcomm-sa8797p-ride-embedded nord Qualcomm SA8797P-Ride-Embedded
%boardfiles arduino-imola qcm2290 Arduino Imola
%boardfiles thundercomm-rb1 qcm2290 Thundercomm RB1
%boardfiles qualcomm-qcm6490-idp qcm6490 Qualcomm QCM6490-IDP
%boardfiles thundercomm-rb3gen2 qcm6490 Thundercomm RB3gen2
%boardfiles qualcomm-qcs615-ride qcs615 Qualcomm QCS615-RIDE
%boardfiles thundercomm-rubikpi3 qcs6490 Thundercomm RubikPi3
%boardfiles radxa-dragon-q6a qcs6490 radxa dragon-q6a
%boardfiles arduino-monza qcs8300 Arduino Monza
%boardfiles qualcomm-iq8275-evk qcs8300 Qualcomm IQ8275-EVK
%boardfiles qualcomm-monaco-draco-evk qcs8300 Qualcomm Monaco-Draco-EVK
%boardfiles qualcomm-qcs8300-ride qcs8300 Qualcomm QCS8300-RIDE
%boardfiles thundercomm-rb2 qrb4210 Thundercomm RB2
%boardfiles qualcomm-iq9075-evk sa8775p Qualcomm IQ9075-EVK
%boardfiles qualcomm-lemans-draco-evk sa8775p Qualcomm Lemans-Draco-EVK
%boardfiles qualcomm-sa8775p-ride sa8775p Qualcomm SA8775P-RIDE
%boardfiles qualcomm-sdm845-hdk sdm845 Qualcomm SDM845-HDK
%boardfiles thundercomm-db845c sdm845 Thundercomm db845c
%boardfiles qualcomm-shikra-cqm-evk shikra Qualcomm Shikra-CQM-EVK
%boardfiles qualcomm-shikra-cqs-evk shikra Qualcomm Shikra-CQS-EVK
%boardfiles qualcomm-shikra-iqs-evk shikra Qualcomm Shikra-IQS-EVK
%boardfiles thundercomm-rb5 sm8250 Thundercomm RB5
%boardfiles qualcomm-sm8750-mtp sm8750 Qualcomm SM8750-MTP
%boardfiles qualcomm-hamoa-iot-evk x1e80100 Qualcomm Hamoa-IoT-EVK
%boardfiles qualcomm-purwa-iot-evk x1p42100 Qualcomm Purwa-IoT-EVK
%boardfiles qualcomm-db410c

%changelog
%autochangelog
