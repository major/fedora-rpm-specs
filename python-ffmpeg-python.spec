%global modname ffmpeg
%global projname %{modname}-python

# Tests require ffmpeg with MPEG4/H264 decoding abilities -
# disable them by default
%bcond_with tests

Name:           python-%{projname}
Version:        0.2.0
Release:        %autorelease
Summary:        Python bindings for FFmpeg - with complex filtering support

License:        Apache-2.0
URL:            https://github.com/kkroening/%{projname}
Source0:        %{url}/archive/%{version}/%{projname}-%{version}.tar.gz
# Rebased version of: https://github.com/kkroening/ffmpeg-python/pull/795
Patch:          remove-dependency-on-future.patch

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  /usr/bin/ffmpeg
%endif

%global _description %{expand:
There are tons of Python FFmpeg wrappers out there but they seem to lack complex
filter support. ffmpeg-python works well for simple as well as complex signal
graphs.}

%description %_description

%package     -n python3-%{projname}
Summary:        %{summary}
Requires:       /usr/bin/ffmpeg

%description -n python3-%{projname} %_description

%prep
%autosetup -n %{projname}-%{version} -p1

%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -t
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%if %{with tests}
%tox
%else
%pyproject_check_import
%endif

%files -n python3-%{projname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
