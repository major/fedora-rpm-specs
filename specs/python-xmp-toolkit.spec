Name:           python-xmp-toolkit
Version:        2.1.0
Release:        %autorelease
Summary:        Python XMP Toolkit for working with metadata

License:        BSD-3-Clause
URL:            https://github.com/python-xmp-toolkit/python-xmp-toolkit
Source:         %pypi_source python_xmp_toolkit

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  exempi
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)

%description
Python XMP Toolkit Python XMP Toolkit is a library for working with XMP
metadata, as well as reading/writing XMP metadata stored in many different file
formats.

%package -n     python3-xmp-toolkit
Summary:        %{summary}

Requires:       exempi

%description -n python3-xmp-toolkit
Python XMP Toolkit Python XMP Toolkit is a library for working with XMP
metadata, as well as reading/writing XMP metadata stored in many different file
formats.


%package -n python-xmp-toolkit-doc
Summary:        python-xmp-toolkit documentation

%description -n python-xmp-toolkit-doc
Documentation for python-xmp-toolkit


%prep
%autosetup -n python_xmp_toolkit-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
PYTHONPATH="$PWD/build/lib" sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l libxmp

%check
%{pytest}

%files -n python3-xmp-toolkit -f %{pyproject_files}
%doc README.rst

%files -n python-xmp-toolkit-doc
%doc html
%license LICENSE

%changelog
%autochangelog
