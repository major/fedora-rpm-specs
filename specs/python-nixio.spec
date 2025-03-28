%global forgeurl    https://github.com/G-node/nixpy

%global desc \
The NIX project started as an initiative within the Electrophysiology Task \
Force a part of the INCF Data sharing Program. The NIX data model allows to \
store fully annotated scientific data-set, i.e. the data together with its \
metadata within the same container. Our aim is to achieve standardization by \
providing a common/generic data structure for a multitude of data types. See \
the wiki for more information \
 \
The current implementations store the actual data using the HDF5 file format as \
a storage backend.

Name:       python-nixio
Version:    1.5.4
Release:    %autorelease
Summary:    Python bindings for NIX

%global     tag     %version
%forgemeta

License:    BSD-3-Clause
URL:        %forgeurl
# We need to upload a filtered version of the source archive because
# docs/source/examples/lenna.png has several issues, including the lack of a
# license. We have asked upstream to deal with this in
#   Please consider replacing lenna.png
#   https://github.com/G-Node/nixpy/issues/545
# but for now, we must obtain the filtered archive by running the script in
# Source2:
#   ./get_source ${VERSION}
%dnl Source0:    %forgesource
Source0:    nixpy-%{version}-filtered.tar.gz
# The tagged snapshot on GitHub still says "dev" but the manually uploaded
# release does not, so use the info.json from there
# https://github.com/G-Node/nixpy/issues/528
Source1:    info.json
# * Script used to obtain Source0: ./get_source %%{version}
Source2:    get_source

# Remove deprecated pytest-runner dependency
# https://github.com/G-Node/nixpy/pull/547
# Rebased on 1.5.4, without changes to GitHub CI configuration
# https://fedoraproject.org/wiki/Changes/DeprecatePythonPytestRunner
Patch:          0001-Remove-deprecated-pytest-runner-dependency.patch

BuildArch:      noarch
# No need for nix, they're uncoupling it from the C++
# https://github.com/G-Node/nixpy/pull/276

BuildRequires:  python3-devel

%description %{desc}

%package -n python3-nixio
Summary:        %{summary}

%description -n python3-nixio %{desc}

%prep
%autosetup -n nixpy-%{version} -p1

# it sets examples_path based on the name of the cwd
sed -i "s/nixpy/nixpy-%{version}/" nixio/test/test_doc_examples.py

cp %{SOURCE1} nixio/info.json -v -p

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l nixio

%check
# These require the removed lenna.png sample file:
k="${k-}${k+ and }not (TestDocumentationExamples and test_image_data)"
k="${k-}${k+ and }not (TestDocumentationExamples and test_image_with_metadata)"
k="${k-}${k+ and }not (TestDocumentationExamples and test_multiple_rois)"
k="${k-}${k+ and }not (TestDocumentationExamples and test_single_roi)"

%pytest -k "${k-}"

%files -n python3-nixio -f %{pyproject_files}
%{_bindir}/nixio

%changelog
%autochangelog
