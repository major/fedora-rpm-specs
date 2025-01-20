# tests are enabled by default
%bcond_without test

%global mod_name kafka
%global project_name %{mod_name}-python
%global with_doc 1

Name:             python-%{mod_name}
Version:          2.0.2
Release:          20%{?dist}
Summary:          Pure Python client for Apache Kafka

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:          Apache-2.0
URL:              https://github.com/dpkp/%{project_name}
Source0:          https://github.com/dpkp/%{project_name}/archive/refs/tags/%{version}.tar.gz
# License file for jslibs using in -doc subpkg
Source1:          LICENSE_doc
# This patch is temporary until upstream stops supporting multi-versioned python.
Patch0:           test_conn.py.patch
# This patch is temporary until upstream stops supporting multi-versioned python.
Patch1:           test_default_records.py.patch
# This patch is temporary until upstream stops supporting multi-versioned python.
Patch2:           test_legacy_records.py.patch
# This patch is temporary until upstream releases 2.0.3. See
# https://github.com/dpkp/kafka-python/pull/2123
Patch3:           setup.py.patch
# This patch is temporary until upstream releases 2.0.3. See
# https://github.com/dpkp/kafka-python/pull/2318
Patch4:           test_assignors.py.patch
# These patches are temporary until upstream releases 2.0.3. See
# https://github.com/dpkp/kafka-python/pull/2376
Patch5:           kafka_codec.py.patch
Patch6:           test_fixture.py.patch
Patch7:           test_codec.py.patch
# This patch is temporary until upstream releases 2.0.3. See
# https://github.com/dpkp/kafka-python/pull/2375
Patch8:           test_client_async.py.patch
# This patch is temporary until upstream releases 2.0.3. See
# https://github.com/dpkp/kafka-python/pull/2438
Patch9:           test_records.py.patch

BuildArch:        noarch
BuildRequires:    pyproject-rpm-macros
BuildRequires:    python3-devel
BuildRequires:    python3-pip
BuildRequires:    python3-wheel


%if %{with test}
BuildRequires:    python3-pytest
BuildRequires:    python3-pytest-mock
BuildRequires:    python3-snappy
BuildRequires:    python3-lz4
BuildRequires:    python3-zstandard
BuildRequires:    python3-xxhash
%endif

%global _description %{expand:
This module provides low-level protocol support for Apache Kafka as well as
high-level consumer and producer classes. Request batching is supported by the
protocol as well as broker-aware request routing. Gzip and Snappy compression
is also supported for message sets.}

%description %{_description}

%package -n python3-%{mod_name}
Summary:          %{summary}

%description -n python3-%{mod_name} %_description


%if %{with_doc}
%package -n python-%{mod_name}-doc
Summary:          Documentation for Pure Python client for Apache Kafka
BuildRequires:    make
BuildRequires:    python3-sphinx_rtd_theme
# BSD for sphinx. MIT for jquery.js and underscore.js.
License:          Apache-2.0 AND BSD-2-Clause AND MIT

%description -n python-%{mod_name}-doc
Documentation for Pure Python client for Apache Kafka.
%endif


%prep
%autosetup -p0 -n %{project_name}-%{version}
install -m 644 %{SOURCE1} %{_builddir}/%{project_name}-%{version}/LICENSE_doc

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel
%if %{with_doc}
%make_build doc
rm -rf docs/_build/html/.buildinfo
%endif

%install
%pyproject_install
install -pm 755 kafka/record/_crc32c.py %{buildroot}/%{python3_sitelib}/%{mod_name}/record/_crc32c.py
# Uses the py3_shebang_fix macro manually because pyproject_install macro
# doesn't automatically changes the Python shebangs.
%py3_shebang_fix %{buildroot}/%{python3_sitelib}/%{mod_name}/record/_crc32c.py
%pyproject_save_files %{mod_name}

# Ignores integrational tests requiring network access and tests requiring
# crc32c that is required only for the test and is not packaged in Fedora.
%check
%pytest --ignore="test/test_consumer_integration.py" --ignore="test/record/test_util.py" test

%files -n python3-%{mod_name} -f %{pyproject_files}
%doc AUTHORS.md CHANGES.md README.rst
%license LICENSE

%if %{with_doc}
%files -n python-%{mod_name}-doc
%doc docs/_build/html
%license LICENSE LICENSE_doc
%endif

# LZ4 is an optional compression lib for python-kafka.
# Snappy is an optional compression lib for python-kafka.
%pyproject_extras_subpkg -n python3-kafka lz4 snappy

# ZSTD is an optional compression lib for python-kafka.
# Needs to write the zstd subpackage section manually because
# zstd's extras_requires causes an incorrect dependency.
%package -n python3-%{mod_name}+zstd
Summary: Metapackage for python3-kafka: zstd extras
Requires: python(abi) = %{python3_version}
Requires: python3-kafka = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: python%{python3_version}dist(zstandard)
Provides: python-kafka+zstd = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_version}-kafka+zstd = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_version}dist(kafka-python[zstd]) = %{?epoch:%{epoch}:}%{version}
Provides: python3dist(kafka-python[zstd]) = %{?epoch:%{epoch}:}%{version}

%description -n python3-kafka+zstd
This is a metapackage bringing in zstd extras requires for python3-kafka.
It makes sure the dependencies are installed.

%files -n python3-kafka+zstd


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.2-19
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Python Maint <python-maint@redhat.com> - 2.0.2-17
- Rebuilt for Python 3.13

* Mon Jun 17 2024 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 2.0.2-16
- Applies test_records.py.patch for Python 3.13

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.0.2-15
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 2.0.2-11
- Applies patches for Python 3.12

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 2.0.2-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 2.0.2-8
- Applies test_assignors.py.patch for Python 3.11

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.0.2-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 29 2021 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 2.0.2-5
- Fixes a rpmlint error

* Wed Sep 29 2021 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 2.0.2-4
- Fixes issues on packaging guidelines

* Mon Sep 27 2021 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 2.0.2-3
- Fixes issues on packaging guidelines

* Fri Sep 24 2021 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 2.0.2-2
- Fixes issues on packaging guidelines

* Sun Sep 19 2021 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 2.0.2-1
- Un-retired and update to 2.0.2

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-3
- Subpackage python2-kafka has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Matthias Runge <mrunge@redhat.com> - 1.4.3-1
- rebuild for python 3.7
- modernize spec file
- update to 1.4.3 (rhbz#1306795)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.1-4
- Python 2 binary package renamed to python2-kafka
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 1.3.1-1
- Upstream 1.3.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Pradeep Kilambi <pkilambi@redhat.com> 0.9.4
- Initial package based on python-kafka.

