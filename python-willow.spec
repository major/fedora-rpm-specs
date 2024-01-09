Name:           python-willow
Version:        1.7.0
Release:        %autorelease
Summary:        A single API for multiple Python image libraries

License:        BSD-3-Clause
URL:            https://github.com/wagtail/Willow
Source:         %{url}/archive/v%{version}/willow-%{version}.tar.gz

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(opencv)

%global _description %{expand:
Willow is a simple image library that combines the APIs of Pillow, Wand and
OpenCV. It converts the image between the libraries when necessary.

Willow currently has basic resize and crop operations, face and feature
detection and animated GIF support. New operations and library integrations can
also be easily implemented.}

%description %_description

%package -n python3-willow
Summary:        %{summary}

%description -n python3-willow %_description


%prep
%autosetup -p1 -n Willow-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files willow


%check
%pytest --ignore tests/test_wand.py \
    -k "not test_avif and not test_heic and not test_save_as_avif and not test_save_as_heic and not test_detect_faces"


%files -n python3-willow -f %{pyproject_files}
%doc README.*
%license LICENSE

%changelog
%autochangelog
