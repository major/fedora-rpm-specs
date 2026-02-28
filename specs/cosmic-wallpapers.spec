# Generated using the scripts at # Generated using the scripts at https://forge.fedoraproject.org/cosmic/cosmic-packaging/src/branch/main/scripts

# While our version corresponds to an upstream tag, we still need to define
# these macros in order to set the VERGEN_GIT_SHA and VERGEN_GIT_COMMIT_DATE
# environment variables in multiple sections of the spec file.
%global commit 3c59953e7ee5792efecdb232cb4c7211e7785f52
%global commitdatestring 2026-02-13 12:35:27 -0700
%global cosmic_minver 1.0.8

Name:           cosmic-wallpapers
Version: 1.0.8
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

