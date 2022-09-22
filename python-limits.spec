%bcond_without tests
%bcond_with hiro

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

# Missing python3dist(coredis), python3dist(coredis[hiredis])
%bcond_with async_redis
# Missing python3dist(emcache)
%bcond_with async_memcached
# Missing python3dist(motor)
%bcond_with async_mongodb

%global pypi_name limits

%global _description %{expand:
This package is a python library to perform rate
limiting with commonly used storage backends
(Redis, Memcached & MongoDB).}

Name:           python-%{pypi_name}
Version:        2.6.3
Release:        2%{?dist}
Summary:        Utilities to implement rate limiting using various strategies

License:        MIT
URL:            https://github.com/alisaifee/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

# Update documentation dependencies
#
# - Switch from sphinx_panels -> sphinx_inline_tabs
# - Upgrade to sphinx 5
Patch:          %{url}/commit/9e85aea3e6a01b7ee2630099cd5365f24d101fd6.patch

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%description doc
Documentation for %{name}.

%if %{with async_redis} && %{with async_memcached} && %{with async_mongodb}
%pyproject_extras_subpkg -n python3-%{pypi_name} all
%endif
%if %{with async_redis}
%pyproject_extras_subpkg -n python3-%{pypi_name} async-redis
%endif
%if %{with async_memcached}
%pyproject_extras_subpkg -n python3-%{pypi_name} async-memcached
%endif
%if %{with async_mongodb}
%pyproject_extras_subpkg -n python3-%{pypi_name} async-mongodb
%endif
%pyproject_extras_subpkg -n python3-%{pypi_name} redis rediscluster memcached mongodb

%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm -fv poetry.lock
# We only need to generate the *additional* requirements for testing.  Also, we
# should patch out linting and coverage dependencies
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters).
sed -r -e '/^[[:blank:]]*(-r|coverage|pytest-cov|lovely-pytest-docker)\b/d' \
    requirements/test.txt | tee requirements/test-filtered.txt
sed -r -i '/^[[:blank:]]*(--cov|-K)\b/d' pytest.ini
%if %{without hiro}
sed -r -i '/^[[:blank:]]*(hiro)/d' requirements/test-filtered.txt
%endif
# Allow newer versions of doc dependencies.
#
# Drop unused and possibly unpackageable
# (https://bugzilla.redhat.com/show_bug.cgi?id=1910798) HTML theme.
#
# Missing dependencies (but we can build documentation anyway):
# - python3dist(sphinx-paramlinks)
#
# For now, tolerate Sphinx 4 in addition to the Sphinx 5 desired by upstream;
# the python-sphinx package will catch up shortly.
sed -r -e 's/==/>=/' \
    -e '/^[[:blank:]]*(furo|sphinx-paramlinks)/d' \
    -e 's/(Sphinx>=)5/\14/' \
    requirements/docs.txt | tee requirements/docs-filtered.txt
sed -r -i '/(paramlinks)/d' doc/source/conf.py
# Cannot use remote intersphinx inventories in offline build:
echo 'intersphinx_mapping.clear()' >> doc/source/conf.py

%generate_buildrequires
%if %{with async_redis} && %{with async_memcached} && %{with async_mongodb}
%pyproject_buildrequires -x all %{?with_tests:requirements/test-filtered.txt}
%else
%{pyproject_buildrequires \
  %{?with_tests:requirements/test-filtered.txt} \
  %{?with_doc_pdf:requirements/docs-filtered.txt} \
  %{?with_async_redis:-x async-redis} \
  %{?with_async_memcached:-x async-memcached} \
  %{?with_async_mongodb:-x async-mongodb} \
  -x redis \
  -x rediscluster \
  -x memcached \
  -x mongodb}
%endif

%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C doc latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C doc/build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files limits

%check
%if %{with tests}
%if %{without hiro}
ignore="${ignore-} --ignore=tests/storage/test_memory.py"
ignore="${ignore-} --ignore=tests/aio/storage/test_memory.py"
%endif
# The deselected tests generally require various servers and/or Docker.
m='not integration'
m="${m-}${m+ and }not redis"
m="${m-}${m+ and }not redis_sentinel"
m="${m-}${m+ and }not redis_cluster"
m="${m-}${m+ and }not mongodb"
m="${m-}${m+ and }not memcached"
%pytest ${ignore-} -m "${m-}"
%endif
# Since quite a few upstream tests needed to be deselected, run the import
# “smoke tests” too.
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files doc
%license LICENSE.txt
%if %{with doc_pdf}
%doc doc/build/latex/%{pypi_name}.pdf
%endif


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 2.6.3-1
- Update to 2.6.3 (https://github.com/alisaifee/limits/releases/tag/2.6.3)
- Restore sphinxext-opengraph doc dependency; it is now packaged
- Backport upstream support for Sphinx 5 (fix RHBZ#2105292)

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.6.2-2
- Rebuilt for Python 3.11

* Tue May 24 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 2.6.2-1
- Update to 2.6.2
- Add extras metapackages where dependencies are available
- Use more generated BuildRequires
- Enable some tests
- Build the PDF documentation

* Wed May 11 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.6.1-1
- Initial package
