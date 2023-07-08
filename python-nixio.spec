%global forgeurl    https://github.com/G-node/nixpy

Name:       python-nixio
Version:    1.5.3
Release:    %autorelease
Summary:    Python bindings for NIX

%global     tag     %version
%forgemeta

License:    BSD
URL:        %forgeurl
Source0:    %forgesource
# The tagged snapshot on GitHub still says "dev" but the manually uploaded
# release does not, so use the info.json from there
# https://github.com/G-Node/nixpy/issues/528
Source1:    info.json


BuildArch:      noarch
# No need for nix, they're uncoupling it from the C++
# https://github.com/G-Node/nixpy/pull/276

%description
The NIX project started as an initiative within the Electrophysiology Task
Force a part of the INCF Data sharing Program. The NIX data model allows to
store fully annotated scientific data-set, i.e. the data together with its
metadata within the same container. Our aim is to achieve standardization by
providing a common/generic data structure for a multitude of data types. See
the wiki for more information

The current implementations store the actual data using the HDF5 file format as
a storage backend.

%package -n python3-nixio
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  gcc
# use tests_require which is deprecated
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-runner}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist pillow}
BuildRequires:  %{py3_dist matplotlib}

%description -n python3-nixio
%{description}

%prep
%forgesetup

# it sets examples_path based on the name of the cwd
sed -i "s/nixpy/nixpy-%{version}/" nixio/test/test_doc_examples.py

cp %{SOURCE1} nixio/info.json -v -p

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nixio

%check
%{pytest}

%files -n python3-nixio -f %{pyproject_files}
%{_bindir}/nixio

%changelog
%autochangelog
