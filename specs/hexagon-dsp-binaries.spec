# Payload is Hexagon (QDSP6) ELF executed on the DSP via FastRPC, not host code
# skip dependency generation to avoid bogus soname Provides/Requires
%global __requires_exclude_from ^%{_datadir}/hexagon-dsp/.*
%global __provides_exclude_from ^%{_datadir}/hexagon-dsp/.*
# binutils strip does not understand Hexagon ELF and may corrupt the binaries
%global __strip %{_bindir}/true
# no debuginfo can be extracted from Hexagon ELF objects
%global debug_package %{nil}

Name:		hexagon-dsp-binaries
Version:	20260810
Release:	%autorelease
Summary:	Hexagon DSP binaries for FastRPC

License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
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
%description -n hexagon-dsp-binaries-%{1} \
Hexagon DSP binaries and configuration for %{2}. \
%{?3:Uses DSP binaries from hexagon-dsp-binaries-%{3}.}

# Board list and inter-board linkage follow upstream config.txt
# Install: own DSP payload, Link: symlink into another board's tree
# Standalone boards (Install only)
%boardpkg qualcomm-db820c %{quote:Qualcomm DB820C}
%boardpkg thundercomm-db845c %{quote:Thundercomm DB845C}
%boardpkg thundercomm-rb1 %{quote:Thundercomm RB1}
%boardpkg thundercomm-rb2 %{quote:Thundercomm RB2}
%boardpkg thundercomm-rb5 %{quote:Thundercomm RB5}
%boardpkg thundercomm-rb3gen2 %{quote:Thundercomm RB3 Gen 2}
%boardpkg radxa-dragon-q6a %{quote:Radxa Dragon Q6A}
%boardpkg qualcomm-sa8775p-ride %{quote:Qualcomm SA8775P RIDE}
%boardpkg qualcomm-qcs8300-ride %{quote:Qualcomm QCS8300 RIDE}
%boardpkg qualcomm-qcs615-ride %{quote:Qualcomm QCS615 RIDE}
%boardpkg qualcomm-hamoa-iot-evk %{quote:Qualcomm Hamoa IoT EVK}
%boardpkg qualcomm-sm8750-mtp %{quote:Qualcomm SM8750 MTP}
%boardpkg qualcomm-kaanapali-mtp %{quote:Qualcomm Kaanapali MTP}
%boardpkg qualcomm-glymur-crd %{quote:Qualcomm Glymur CRD}
%boardpkg qualcomm-shikra-cqs-evk %{quote:Qualcomm Shikra CQS EVK}
# Hybrid board (own adsp, cdsp Linked to RB3gen2)
%boardpkg thundercomm-rubikpi3 %{quote:Thundercomm Rubik Pi 3} thundercomm-rb3gen2
# Linked boards (Link only)
%boardpkg qualcomm-sdm845-hdk %{quote:Qualcomm SDM845 HDK} thundercomm-db845c
%boardpkg qualcomm-shikra-cqm-evk %{quote:Qualcomm Shikra CQM EVK} qualcomm-shikra-cqs-evk
%boardpkg qualcomm-shikra-iqs-evk %{quote:Qualcomm Shikra IQS EVK} qualcomm-shikra-cqs-evk
%boardpkg arduino-monza %{quote:Arduino Monza} qualcomm-qcs8300-ride
%boardpkg qualcomm-iq8275-evk %{quote:Qualcomm IQ8275 EVK} qualcomm-qcs8300-ride
%boardpkg qualcomm-iq9075-evk %{quote:Qualcomm IQ9075 EVK} qualcomm-sa8775p-ride
%boardpkg qualcomm-purwa-iot-evk %{quote:Qualcomm Purwa IoT EVK} qualcomm-hamoa-iot-evk
%boardpkg qualcomm-qcm6490-idp %{quote:Qualcomm QCM6490 IDP} thundercomm-rb3gen2
# Conf only
%boardpkg qualcomm-db410c %{quote:Qualcomm DragonBoard 410c}

%prep
%autosetup -n %{name}-%{version}

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
%boardfiles thundercomm-db845c sdm845 Thundercomm db845c
%boardfiles thundercomm-rb1 qcm2290 Thundercomm RB1
%boardfiles thundercomm-rb2 qrb4210 Thundercomm RB2
%boardfiles thundercomm-rb5 sm8250 Thundercomm RB5
%boardfiles thundercomm-rb3gen2 qcm6490 Thundercomm RB3gen2
%boardfiles radxa-dragon-q6a qcs6490 radxa dragon-q6a
%boardfiles thundercomm-rubikpi3 qcs6490 Thundercomm RubikPi3
%boardfiles qualcomm-sa8775p-ride sa8775p Qualcomm SA8775P-RIDE
%boardfiles qualcomm-qcs8300-ride qcs8300 Qualcomm QCS8300-RIDE
%boardfiles qualcomm-qcs615-ride qcs615 Qualcomm QCS615-RIDE
%boardfiles qualcomm-hamoa-iot-evk x1e80100 Qualcomm Hamoa-IoT-EVK
%boardfiles qualcomm-sm8750-mtp sm8750 Qualcomm SM8750-MTP
%boardfiles qualcomm-kaanapali-mtp kaanapali Qualcomm Kaanapali-MTP
%boardfiles qualcomm-glymur-crd glymur Qualcomm Glymur-CRD
%boardfiles qualcomm-shikra-cqs-evk shikra Qualcomm Shikra-CQS-EVK
%boardfiles qualcomm-sdm845-hdk sdm845 Qualcomm SDM845-HDK
%boardfiles qualcomm-shikra-cqm-evk shikra Qualcomm Shikra-CQM-EVK
%boardfiles qualcomm-shikra-iqs-evk shikra Qualcomm Shikra-IQS-EVK
%boardfiles arduino-monza qcs8300 Arduino Monza
%boardfiles qualcomm-iq8275-evk qcs8300 Qualcomm IQ8275-EVK
%boardfiles qualcomm-iq9075-evk sa8775p Qualcomm IQ9075-EVK
%boardfiles qualcomm-purwa-iot-evk x1p42100 Qualcomm Purwa-IoT-EVK
%boardfiles qualcomm-qcm6490-idp qcm6490 Qualcomm QCM6490-IDP
%boardfiles qualcomm-db410c

%changelog
%autochangelog
