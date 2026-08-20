%global forgeurl https://github.com/jim-easterbrook/python-exiv2

Name:           python-exiv2
Version:        0.19.0
Release:        %autorelease
Summary:        Low level Python interface to the Exiv2 C++ library

%global tag %{version}
%forgemeta

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source:         %{forgesource}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

Patch:          python-exiv2-float32-precision.patch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  exiv2-devel
BuildRequires:  gcc-c++
BuildRequires:  git-core

%global _description %{expand:
python-exiv2 is a low level interface (or binding) to the exiv2 C++ library. It
is built using SWIG to automatically generate the interface code. The intention
is to give direct access to all of the top-level classes in libexiv2, but with
additional "Pythonic" helpers where necessary. Not everything in libexiv2 is
available in the Python interface.}

%description %_description

%package -n python3-exiv2
Summary:        %{summary}

%description -n python3-exiv2 %_description

%prep
%forgeautosetup -S git

# remove spurious dep
sed -i 's/"toml"//' pyproject.toml

# remove shebangs
pushd examples
for i in *.py
do
    echo "** $i **"
    sed -i '/^#!\/usr\/bin\/env.*python$/ d' $i
done

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l exiv2

%check
%pyproject_check_import -e '*examples*'

%{pytest} -v

%files -n python3-exiv2 -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
