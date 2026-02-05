%global forgeurl https://github.com/jim-easterbrook/python-exiv2

Name:           python-exiv2
Version:        0.18.0
Release:        %autorelease
Summary:        Low level Python interface to the Exiv2 C++ library

%global tag %{version}
%forgemeta

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source:         %{forgesource}

# skip assertions for py3.14 for the moment
# https://github.com/jim-easterbrook/python-exiv2/issues/56
Patch:          https://github.com/jim-easterbrook/python-exiv2/commit/fe98ad09ff30f1b6cc5fd5dcc0769f9505c09166.patch
Patch:          https://github.com/jim-easterbrook/python-exiv2/commit/e0a5284620e8d020771bf8c1fa73d6113e662ebf.patch
# Another intermittently failing test reported upstream by Benson:
# https://github.com/jim-easterbrook/python-exiv2/issues/57
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
