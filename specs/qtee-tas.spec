Name:		qtee-tas
Version:	0.1.0
Release:	%autorelease
Summary:	Qualcomm TEE Trusted Applications

License:	LicenseRef-Fedora-Firmware
URL:		https://github.com/qualcomm/qtee-tas
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc

ExclusiveArch:	%{arm64}

BuildArch:	noarch

%description
Qualcomm-signed Trusted Applications (TAs) for the Qualcomm Trusted
Execution Environment (QTEE). The TAs run in the secure world and offer
TEE-backed key storage and cryptographic operations, secure storage and
TEE stack validation to normal-world client applications.

Supported platforms include Glymur, Kaanapali, Mahua, QCM2290, QCM6490,
QCS615, QCS8300, QCS9100, Shikra, SM8750, X1E80100 and X1P42100.

%prep
%autosetup

%build
# Nothing to compile

%install
install -d %{buildroot}%{_prefix}/lib/qtee-tas
cp -a ta/* %{buildroot}%{_prefix}/lib/qtee-tas

%files
%license LICENSE.txt NO.LOGIN.BINARY.LICENSE.QTI.pdf
%doc README.md
%{_prefix}/lib/qtee-tas

%changelog
%autochangelog
