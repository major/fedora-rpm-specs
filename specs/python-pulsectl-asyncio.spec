Name:           python-pulsectl-asyncio
Version:        1.3.1
Release:        %{autorelease}
Summary:        Asyncio frontend for the pulsectl Python bindings of libpulse
License:        MIT
URL:            https://github.com/mhthies/pulsectl-asyncio
Source0:        %{pypi_source pulsectl_asyncio}

BuildArch:      noarch
BuildRequires:  /usr/bin/paplay
BuildRequires:  /usr/bin/pulseaudio
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
# The tests in tests/test_examples.py depend on the contents of the
# examples/ directory, which is present in Git but absent from the
# release tarball.
rm tests/test_examples.py

%{py3_test_envvars} %{python3} -m unittest discover

%pyproject_check_import


%files -n python3-pulsectl-asyncio -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
