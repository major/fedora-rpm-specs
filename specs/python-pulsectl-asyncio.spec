Name:           python-pulsectl-asyncio
Version:        1.2.2
Release:        %{autorelease}
Summary:        Asyncio frontend for the pulsectl Python bindings of libpulse
License:        MIT
URL:            https://github.com/mhthies/pulsectl-asyncio
Source0:        %{pypi_source pulsectl_asyncio}

# https://github.com/mhthies/pulsectl-asyncio/commit/c1e5587bcec8f976580e2291518497388eb88109
Patch:          python-pulsectl-24.12.0.diff

BuildArch:      noarch
# BuildRequires:  /usr/bin/pulseaudio
BuildRequires:  pulseaudio-libs
BuildRequires:  python3-devel

%global _description %{expand:
A Python 3 asyncio interface on top of the pulsectl library for monitoring and
controlling the PulseAudio sound server.}

%description %_description


%package -n python3-pulsectl-asyncio
Summary:        %{summary}

%description -n python3-pulsectl-asyncio %_description


%prep
%autosetup -p1 -n pulsectl_asyncio-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pulsectl_asyncio


%check
## https://github.com/mhthies/pulsectl-asyncio/issues/15
# touch tests/__init__.py

## These test fail, because they cause the puleseaudio daemon to crash.
## Perhaps this doesn't matter, because users will typically be using
## pipewire-pulse instead.
## https://github.com/mhthies/pulsectl-asyncio/issues/16
# %%{py3_test_envvars} %%{python3} -m unittest discover

%pyproject_check_import


%files -n python3-pulsectl-asyncio -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
