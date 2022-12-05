# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-gcsfs
Version:        2022.11.0
Release:        1%{?dist}
Summary:        Convenient Filesystem interface over GCS

License:        BSD-3-Clause
URL:            https://github.com/fsspec/gcsfs
# We must use the GitHub archive rather than the PyPI sdist if we want to have
# all the necessary files to build the Sphinx docs.
Source0:        %{url}/archive/%{version}/gcsfs-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# Testing:
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(vcrpy)
# Docs:
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%description
Pythonic file-system for Google Cloud Storage.

%package -n     python3-gcsfs
Summary:        %{summary}

%description -n python3-gcsfs
Pythonic file-system for Google Cloud Storage.

%pyproject_extras_subpkg -n python3-gcsfs gcsfuse,crc

%package -n python-gcsfs-doc
Summary:        Documentation for gcsfs

%description -n python-gcsfs-doc
Documentation for gcsfs.

%prep
%autosetup -n gcsfs-%{version}
# We cannot respect version pins:
sed -r -i 's/<.*//' docs/requirements.txt
# Do not pin the exact corresponding version of fsspec; this makes sense on
# PyPI since both are developed under the same organization and have
# coordinated releases, but it’s unlikely we’ll be able to maintain this level
# of coordination downstream, and it’s better to have “possible” breakage from
# version skew than *guaranteed* breakage from version skew.
sed -r -i 's/==.*//' requirements.txt

%generate_buildrequires
%pyproject_buildrequires -x gcsfuse,crc %{?with_doc_pdf:docs/requirements.txt}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gcsfs
%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/build/latex LATEXMKOPTS='-quiet'
%endif

%check
# The package has tests, but nearly all require network access and/or cloud
# resources, so we do an import-only “smoke test” instead.
#
# gcsfs.cli.gcsfuse imports click (which is not otherwise required) and also
# tries to import a nonexistent 'gcsfs.gcsfuse' module; this seems like a bug
%pyproject_check_import -e 'gcsfs.cli.gcsfuse'

%files -n python3-gcsfs -f %{pyproject_files}
%doc README.rst

%files -n python-gcsfs-doc
%if %{with doc_pdf}
%doc docs/build/latex/GCSFs.pdf
%endif
%license LICENSE.txt

%changelog
* Wed Nov 23 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 2022.11.0-1
- Update to 2022.11.0 (close RHBZ#2130978, close RHBZ#2136233)

* Wed Nov 23 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.6.2-10
- Convert to pyproject-rpm-macros
- Properly package the Extras subpackage for gcsfuse
- Update License to SPDX
- Update URL
- Build Sphinx docs as PDF instead of HTML due to issues of bundling, etc.
- Fix spurious executable permission on pbr.json in dist-info

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 0.6.2-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.2-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.2-2
- Condition for tests
- Update BR (rhbz#1836686)

* Sun May 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.2-1
- Initial package for Fedora
