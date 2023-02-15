%global srcname patatt

Name:           python-%{srcname}
Version:        0.6.3
Release:        %autorelease
Summary:        Add cryptographic attestation to patches sent via email
License:        MIT-0
URL:            https://git.kernel.org/pub/scm/utils/%{srcname}/%{srcname}.git
Source0:        https://mirrors.edge.kernel.org/pub/software/devel/%{srcname}/%{srcname}-%{version}.tar.xz
Source1:        https://mirrors.edge.kernel.org/pub/software/devel/%{srcname}/%{srcname}-%{version}.tar.sign
# https://git.kernel.org/pub/scm/utils/patatt/patatt.git/plain/.keys/openpgp/linuxfoundation.org/konstantin/default
Source2:        gpgkey-DE0E66E32F1FDD0902666B96E63EDCA9329DD07E.asc

BuildArch:      noarch

BuildRequires:  gnupg2
BuildRequires:  python%{python3_pkgversion}-devel

%global _description %{expand:
This utility allows an easy way to add end-to-end cryptographic attestation to
patches sent via mail. It does so by adapting the DKIM email signature standard
to include cryptographic signatures via the X-Developer-Signature email header.}

%description %{_description}


%package -n %{srcname}
Summary:        %{summary}
Provides:       python%{python3_pkgversion}-%{srcname} = %{version}-%{release}

%description -n %{srcname} %{_description}


%prep
xz -dc '%{SOURCE0}' | %{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=-
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r requirements.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import


%files -n %{srcname} -f %{pyproject_files}
%license COPYING
%doc DCO README.rst samples
%{_bindir}/%{srcname}
%{_mandir}/man5/%{srcname}.5.*


%changelog
%autochangelog
