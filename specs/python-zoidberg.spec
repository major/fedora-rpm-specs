# Created by pyp2rpm-3.3.4
Name:           python-zoidberg
Version:        0.2.1
Release:        %{autorelease}
Summary:        A Flux-Coordinate Independent (FCI) Grid Generator for BOUT++

License:        LGPL-3.0-or-later
URL:            http://boutproject.github.io
Source0:        %{pypi_source zoidberg}
BuildArch:      noarch

Patch:          https://github.com/boutproject/zoidberg/pull/38.patch#./version.patch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-pytest

%description
A Flux-Coordinate Independent (FCI) Grid Generator for BOUT++

%package -n     python3-zoidberg
Summary:        %{summary}

%description -n python3-zoidberg
A Flux-Coordinate Independent (FCI) Grid Generator for BOUT++

%generate_buildrequires
%pyproject_buildrequires -r


%prep
%autosetup -n zoidberg-%{version} -p 1
# Remove bundled egg-info
rm -rf zoidberg.egg-info


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files zoidberg


%check
# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1997717
export HDF5_USE_FILE_LOCKING=FALSE
%pytest


%files -n python3-zoidberg -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/zoidberg-*


%changelog
%{autochangelog}
