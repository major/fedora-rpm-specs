Name:           python-blobfile
Version:        3.0.0
Release:        %autorelease
Summary:        Read GCS, ABS and local paths with the same interface

License:        Unlicense
URL:            https://github.com/blobfile/blobfile
Source:         %{pypi_source blobfile}

BuildArch:      noarch
BuildRequires:  python3-devel
# BuildRequires to convert README.md
BuildRequires:  dos2unix
# BuildRequires for testing
#BuildRequires:  python3dist(xmltodict)
#BuildRequires:  python3dist(lxml)


%global _description %{expand:
This is a library that provides a Python-like interface for reading local and
remote files (only from blob storage), with an API similar to open() as well as
some of the os.path and shutil functions. blobfile supports local paths, Google
Cloud Storage paths (gs://<bucket>), and Azure Blob Storage paths
(az://<account>/<container>
or https://<account>.blob.core.windows.net/<container>/).

The main function is BlobFile, which lets you open local and remote files that
act more or less like local ones. There are also a few additional functions
such as basename, dirname, and join, which mostly do the same thing as their
os.path namesakes, only they also support GCS paths and ABS paths.

This library is inspired by TensorFlow's gfile but does not have exactly the
same interface.
}

%description %_description

%package -n     python3-blobfile
Summary:        %{summary}

%description -n python3-blobfile %_description


%prep
%autosetup -p1 -n blobfile-%{version}
/usr/bin/dos2unix -k README.md
# Remove the test files, not needed for normal operation.
# We cannot use them, (see below,) so remove them.
# See: https://github.com/blobfile/blobfile/issues/226
rm blobfile/_ops_test.py
rm blobfile/_xml_test.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l blobfile


%check
%pyproject_check_import
# Run the XML benchmarks/tests since those work offline
# Except they don't actually work 
# See upstream bug: https://github.com/blobfile/blobfile/issues/257
#/usr/bin/python3 -m blobfile._xml_test
# We could run tests with python testing/run.py --direct but
# "The tests are rather slow, ~7 minutes to run (even though large file tests
# are disabled) and require accounts with every cloud provider."
# Upstream bug: https://github.com/blobfile/blobfile/issues/256


%files -n python3-blobfile -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
