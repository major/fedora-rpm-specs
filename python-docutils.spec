Name:           python-docutils
Version:        0.20.1
Release:        %autorelease
Summary:        System for processing plaintext documentation

# See COPYING.txt for information
# PSF-2.0 was chosen for the SPDX identifier as it's the spirit of the original
# author's notice, even though the shipped license text is copied from Python 2.1.1
# See: https://gitlab.com/fedora/legal/fedora-license-data/-/issues/216
License:        LicenseRef-Fedora-Public-Domain AND BSD-2-Clause AND BSD-3-Clause AND PSF-2.0 AND GPL-3.0-or-later
URL:            https://docutils.sourceforge.net
Source0:        https://sourceforge.net/projects/docutils/files/docutils/%{version}/docutils-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}-devel

%global _description %{expand:
The Docutils project specifies a plaintext markup language, reStructuredText,
which is easy to read and quick to write.  The project includes a python
library to parse rST files and transform them into other useful formats such
as HTML, XML, and TeX as well as commandline tools that give the enduser
access to this functionality.

Currently, the library supports parsing rST that is in standalone files and
PEPs (Python Enhancement Proposals).  Work is underway to parse rST from
Python inline documentation modules and packages.}

%description %_description


%package -n python%{python3_pkgversion}-docutils
Summary:        %{summary}

%description -n python%{python3_pkgversion}-docutils %_description


%prep
%autosetup -p1 -n docutils-%{version}

# Remove shebang from library files
sed -i -e '/#! *\/usr\/bin\/.*/{1D}' $(grep -Erl '^#!.+python' docutils)

# We want the licenses but don't need this build file
rm -f licenses/docutils.conf


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files docutils

for file in %{buildroot}%{_bindir}/*.py; do
  mv $file $(dirname $file)/$(basename $file .py)
done


%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{python3} test/alltests.py


%files -n python%{python3_pkgversion}-docutils -f %{pyproject_files}
%license COPYING.txt licenses/*
%doc BUGS.txt FAQ.txt HISTORY.txt README.txt RELEASE-NOTES.txt THANKS.txt
%{_bindir}/rst*
%{_bindir}/docutils


%changelog
%autochangelog
