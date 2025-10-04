Name:           python-playsound3
Version:        3.2.8
Release:        %autorelease
Summary:        Cross-platform library to play audio files

License:        MIT
URL:            https://github.com/sjmikler/playsound3
Source:         %{pypi_source playsound3}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Cross platform library to play sound files in Python.}

%description %_description

%package -n     python3-playsound3
Summary:        %{summary}
Recommends:     gstreamer1-plugins-base-tools

%description -n python3-playsound3 %_description


%prep
%autosetup -p1 -n playsound3-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l playsound3


%check
%pyproject_check_import
#tests play sounds and don't work reliably in an rpm build.

%files -n python3-playsound3 -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
