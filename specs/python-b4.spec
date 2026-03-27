%global srcname b4

%if 0%{?fedora} || 0%{?el10}
%bcond_without attest
%else
# some attestation dependencies not in EPEL
%bcond_with attest
%endif

Name:           python-%{srcname}
Version:        0.14.3
Release:        %autorelease
Summary:        A helper tool to work with public-inbox and patch series
License:        GPL-2.0-or-later
URL:            https://git.kernel.org/pub/scm/utils/%{srcname}/%{srcname}.git
Source0:        https://mirrors.edge.kernel.org/pub/software/devel/%{srcname}/%{srcname}-%{version}.tar.xz
Source1:        https://mirrors.edge.kernel.org/pub/software/devel/%{srcname}/%{srcname}-%{version}.tar.sign
# https://git.kernel.org/pub/scm/utils/b4/b4.git/plain/.keys/openpgp/linuxfoundation.org/konstantin/default
Source2:        gpgkey-DE0E66E32F1FDD0902666B96E63EDCA9329DD07E.asc

BuildArch:      noarch

BuildRequires:  gnupg2
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(shtab)

%global _description %{expand:
B4 is a helper utility to work with patches made available via a public-inbox
archive like lore.kernel.org. It is written to make it easier to participate in
a patch-based workflows, like those used in the Linux kernel development.}

%description %{_description}


%package -n %{srcname}
Summary:        %{summary}
Provides:       python%{python3_pkgversion}-%{srcname} = %{version}-%{release}

%description -n %{srcname} %{_description}


%prep
xz -dc '%{SOURCE0}' | %{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=-
%autosetup -p1 -n %{srcname}-%{version}

# Disable attestation (only applicable to EPEL)
%if %{without attest}
sed -Ei -e '/^# These are optional, needed for attestation/d' \
    -e "/^ *'?(dnspython|dkimpy|patatt)/d" requirements.in
%endif


%generate_buildrequires
%pyproject_buildrequires -r requirements.in


%build
%pyproject_wheel
misc/tc-generate.sh bash > b4-completion-bash
misc/tc-generate.sh zsh > b4-completion-zsh


%install
%pyproject_install
%pyproject_save_files %{srcname}
install -m644 -Dt %{buildroot}%{_mandir}/man5/ src/b4/man/b4.5
install -m644 -D b4-completion-bash %{buildroot}%{_datadir}/bash-completion/completions/b4
install -m644 -D b4-completion-zsh %{buildroot}%{_datadir}/zsh/site-functions/_b4


%check
%pyproject_check_import
%pytest


%files -n %{srcname} -f %{pyproject_files}
%doc README.rst
%{_bindir}/%{srcname}
%{_mandir}/man5/%{srcname}.5.*
%{_datadir}/bash-completion/completions/b4
%{_datadir}/zsh/site-functions/_b4


%changelog
%autochangelog
