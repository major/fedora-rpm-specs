# Generated using the scripts at # Generated using the scripts at https://forge.fedoraproject.org/cosmic/cosmic-packaging/src/branch/main/scripts

# While our version corresponds to an upstream tag, we still need to define
# these macros in order to set the VERGEN_GIT_SHA and VERGEN_GIT_COMMIT_DATE
# environment variables in multiple sections of the spec file.
%global commit d6c60281508ef6b20db712612dad256d0b44b4fb
%global commitdatestring 2026-08-21 11:49:16 -0600
%global cosmic_minver 1.8.0

Name:           cosmic-wallpapers
Version: 1.8.0
Release:        %autorelease
Summary:        Default wallpapers for the COSMIC Desktop Environment

# All cosmic wallpapers are either public domain or CC-BY-SA-4.0
License:        CC-BY-SA-4.0

URL:            https://github.com/pop-os/cosmic-wallpapers

# How to recreate this source
# Install git-lfs
# Clone https://github.com/pop-os/cosmic-wallpapers
# Checkout commit %%{commit}
# dnf install git-lfs
# git clone https://github.com/pop-os/cosmic-wallpapers
# cd cosmic-wallpapers && git checkout %%{commit} && cd ..
# tar -pczf cosmic-wallpapers-%%{version_no_tilde}.tar.gz cosmic-wallpapers
Source0:        cosmic-wallpapers-%{version_no_tilde}.tar.gz

BuildArch:      noarch

BuildRequires:  make

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
tar -xzf %{SOURCE0} -C .

%build

%install
cd cosmic-wallpapers
# Set vergen environment variables
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
make install DESTDIR=%{buildroot} prefix=%{_prefix}

%files
%dir %{_datadir}/backgrounds/cosmic
%{_datadir}/backgrounds/cosmic/*
%license cosmic-wallpapers/LICENSE

%changelog
%autochangelog

