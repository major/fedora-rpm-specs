# Generated using the scripts at # Generated using the scripts at https://forge.fedoraproject.org/cosmic/cosmic-packaging/src/branch/main/scripts

# While our version corresponds to an upstream tag, we still need to define
# these macros in order to set the VERGEN_GIT_SHA and VERGEN_GIT_COMMIT_DATE
# environment variables in multiple sections of the spec file.
%global commit 6fafded5edfff7693224f3ccf01b861896c35f3e
%global commitdatestring 2026-04-15 01:25:45 +0200
%global cosmic_minver 1.0.11

Name:           cosmic-icon-theme
Version: 1.0.11
Release:        %autorelease
Summary:        Icon theme for the COSMIC Desktop Environment

License:        CC-BY-SA-4.0

URL:            https://github.com/pop-os/cosmic-icons

Source0:        https://github.com/pop-os/cosmic-icons/archive/epoch-%{version_no_tilde}/cosmic-icons-%{version_no_tilde}.tar.gz

BuildArch:      noarch

BuildRequires:  just


Requires:       pop-icon-theme

Obsoletes: cosmic-icons < 0.1.0~git20240526.04.9aad1ab-2
Provides:  cosmic-icons = %{version}-%{release}

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n cosmic-icons-epoch-%{version_no_tilde}

%build

%install
# Set vergen environment variables
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%dir %{_datadir}/icons/Cosmic
%{_datadir}/icons/Cosmic/*

%changelog
%autochangelog

