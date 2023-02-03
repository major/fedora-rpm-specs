%global desc %{expand: \
The Virtual Brain Project (TVB Project) has the purpose of offering some modern
tools to the Neurosciences community, for computing, simulating and analyzing
functional and structural data of human brains.

The gdist module is a Cython interface to a C++ library
(http://code.google.com/p/geodesic/) for computing geodesic distance which is
the length of shortest line between two vertices on a triangulated mesh in
three dimensions, such that the line lies on the surface.

The algorithm is due Mitchell, Mount and Papadimitriou, 1987; the
implementation is due to Danil Kirsanov and the Cython interface to Gaurav
Malhotra and Stuart Knock.

Original library (published under MIT license):
http://code.google.com/p/geodesic/

We added a python wrapped and made small fixes to the original library, to make
it compatible with cython.
}

Name:           python-tvb-gdist
Version:        2.1.1
Release:        %autorelease
Summary:        Cython interface to geodesic

License:        GPL-3.0-or-later
URL:            https://pypi.python.org/pypi/tvb-gdist
Source0:        %{pypi_source tvb-gdist}

%description
%{desc}

%package -n python3-tvb-gdist
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gcc-c++

%description -n python3-tvb-gdist
%{desc}

%prep
%autosetup -n tvb-gdist-%{version}
# They delete the build folder for some reason
sed -i '/rmtree/ d' setup.py

# Set cython language level
sed -i '2 a # cython: language_level=3' gdist.pyx

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gdist

%check
%pyproject_check_import

%files -n python3-tvb-gdist -f %{pyproject_files}

%changelog
%autochangelog
