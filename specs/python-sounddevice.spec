Name:           python-sounddevice
Version:        0.5.3
Release:        %autorelease
Summary:        Play and record sound with Python

License:        MIT
URL:            https://github.com/spatialaudio/python-sounddevice
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  portaudio

%global _description %{expand:
Play and record sound with Python.}

%description %_description

%package -n python3-sounddevice
Summary:        %{summary}

%description -n python3-sounddevice %_description


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l sounddevice _sounddevice


%check
%pyproject_check_import


%files -n python3-sounddevice -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
