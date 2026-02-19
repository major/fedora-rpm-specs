%global pypi_name webrtcvad

Name:           python-%{pypi_name}
Version:        2.0.10
Release:        1%{?dist}
Summary:        Python interface to the WebRTC Voice Activity Detector

License:        MIT
URL:            https://github.com/wiseman/py-webrtcvad
Source0:        %{pypi_source}
Patch0: 001-add-ppc64le_s390x-support.patch
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
This is a python interface to the WebRTC Voice Activity Detector (VAD). 
A VAD classifies a piece of audio data as being voiced or unvoiced. 
It can be useful for telephony and speech recognition.

%package -n python3-%{pypi_name}
Summary:        %{summary}
%py_provides python3-%{pypi_name}

%description -n python3-%{pypi_name}
This is a python interface to the WebRTC Voice Activity Detector (VAD). 
A VAD classifies a piece of audio data as being voiced or unvoiced. 
It can be useful for telephony and speech recognition.

%prep
%setup -n %{pypi_name}-%{version}
%patch 0 -p1 -b .orig~

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name} _%{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files} 
%license LICENSE
%doc README.rst

%changelog
* Wed Jan 28 2026 Manish Tiwari <matiwari@redhat.com> 2.0.10-1
- Initial release of the package
