Summary:        Viewer for Hierarchical Datafiles (HDF5)
Name:           ViTables
Version:        3.0.2
Release:        %autorelease
License:        GPLv3
URL:            https://www.vitables.org/

Source0:        https://github.com/uvemas/ViTables/archive/v%{version}/vitables-%{version}.tar.gz
Patch:          vitables-collections-import.patch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-numpy
BuildRequires:  python3-tables
BuildRequires:  hdf5-devel
BuildRequires:  python3-sphinx

BuildArch:      noarch

%global _description %{expand:
ViTables is a component of the PyTables family. It is a graphical tool
for browsing and editing files in both PyTables and HDF5 formats. It
is developed using Python and PyQt (the Python binding to the Qt
library), so it can run on any platform that supports these components.}

%description %_description

%package -n vitables
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < 3.0.0-1
Requires:       hdf5
Requires:       python3-numpy
Requires:       python3-tables
Requires:       python3-qt5
Requires:       python3-QtPy

%description -n vitables %_description

%package -n vitables-doc
Summary:        vitables documentation and examples
Requires:       vitables = %{version}-%{release}

%description -n vitables-doc
This package contains the documentation and examples for vitables.

%prep
%autosetup -p1

%build
%py3_build
make -C doc html

%install
%py3_install

# force the directory to be the same for ViTables and ViTables-doc
%global _docdir_fmt vitables

%files -n vitables
%license LICENSE.txt
%doc ANNOUNCE.txt README.txt TODO.txt
%{_bindir}/vitables
%{python3_sitelib}/vitables
%{python3_sitelib}/%{name}-%{version}-py*.egg-info

%files -n vitables-doc
%doc examples/
%doc doc/_build/html/

%changelog
%autochangelog
