Name:           python-waitress
Version:        3.0.2
Release:        %autorelease
Summary:        Waitress WSGI server

License:        ZPL-2.1
URL:            https://github.com/Pylons/waitress
Source0:        waitress-%{version}-nodocs.tar.gz
# Upstream ships non free docs files.
#
# https://github.com/Pylons/waitress/issues/78
#
# We do not even want them in our src.rpms
# So we remove them before uploading.
#
# Download the upstream tarball and invoke this script while in the
# tarball's directory:
# ./generate-tarball.sh 1.0
#
Source1: generate-tarball.sh

BuildArch:      noarch

%global _description %{expand:
Waitress is a production-quality pure-Python WSGI server with very acceptable
performance. It has no dependencies except ones which live in the Python
standard library.}

%description %{_description}

%package -n python3-waitress
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-waitress %{_description}

%prep
%autosetup -n waitress-%{version}-nodocs
sed -e '/pytest-cov/d' \
    -e '/coverage/d' \
    -e '/addopts/d' \
    -i setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x testing

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l waitress

%check
%pytest

%files -n python3-waitress -f %{pyproject_files}
%doc README.rst CHANGES.txt
%{_bindir}/waitress-serve

%changelog
%autochangelog
