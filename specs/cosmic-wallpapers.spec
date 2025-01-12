# Generated using the scripts at https://pagure.io/fedora-cosmic/cosmic-packaging/blob/main/f/scripts

# While our version corresponds to an upstream tag, we still need to define
# these macros in order to set the VERGEN_GIT_SHA and VERGEN_GIT_COMMIT_DATE
# environment variables in multiple sections of the spec file.
%global commit cb8e6d653b5062e046e83b4670c3d9944fa39c39
%global commitdatestring 2024-10-31 12:00:42 -0600
%global cosmic_minver 1.0.0~alpha.5

Name:           cosmic-wallpapers
Version:        1.0.0~alpha.5
Release:        %autorelease
Summary:        Default wallpapers for the COSMIC Desktop Environment

# All cosmic wallpapers are either public domain or CC-BY-SA-4.0
License:        CC-BY-SA-4.0

URL:            https://github.com/pop-os/cosmic-wallpapers

Source0:        https://github.com/pop-os/cosmic-wallpapers/archive/epoch-%{version_no_tilde}/cosmic-wallpapers-%{version_no_tilde}.tar.gz

# https://github.com/pop-os/cosmic-wallpapers/pull/7
Patch0:         https://patch-diff.githubusercontent.com/raw/pop-os/cosmic-wallpapers/pull/7.patch

BuildArch:      noarch

BuildRequires:  make

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n cosmic-wallpapers-epoch-%{version_no_tilde} -p1

%build

%install
# Set vergen environment variables
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
make install DESTDIR=%{buildroot} prefix=%{_prefix}

%files
%dir %{_datadir}/backgrounds/cosmic
%{_datadir}/backgrounds/cosmic/*
%license LICENSE

%changelog
%autochangelog
    
