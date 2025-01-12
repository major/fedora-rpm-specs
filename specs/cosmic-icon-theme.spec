# Generated using the scripts at https://pagure.io/fedora-cosmic/cosmic-packaging/blob/main/f/scripts

# While our version corresponds to an upstream tag, we still need to define
# these macros in order to set the VERGEN_GIT_SHA and VERGEN_GIT_COMMIT_DATE
# environment variables in multiple sections of the spec file.
%global commit 3fdc2175c145e00d798f98e81d5c4d493f0a2a8c
%global commitdatestring 2024-10-02 15:51:55 -0600
%global cosmic_minver 1.0.0~alpha.5

Name:           cosmic-icon-theme
Version:        1.0.0~alpha.5
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
just rootdir=%{buildroot} install

%files
%dir %{_datadir}/icons/Cosmic
%{_datadir}/icons/Cosmic/*

%changelog
%autochangelog
    
