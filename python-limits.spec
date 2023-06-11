%bcond_without tests
%bcond_with hiro

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

%if 0%{?fc36}
# python3dist(redis) is too old
%bcond_with redis
%else
%bcond_without redis
%endif
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
Version:        2.8.0
Release:        %autorelease
Summary:        Utilities to implement rate limiting using various strategies

# SPDX
License:        MIT
URL:            https://github.com/alisaifee/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
%if %{without redis}
# Even though redis is too old for the redis extra, we still need it for
# test_lazy_dependency_found and test_lazy_dependency_version_low.
BuildRequires:  python3dist(redis)
%endif

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

%if %{with async_redis} && %{with async_memcached} && %{with async_mongodb} && %{with redis}
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
%if %{with redis}
%pyproject_extras_subpkg -n python3-%{pypi_name} redis rediscluster
%endif
%pyproject_extras_subpkg -n python3-%{pypi_name} memcached mongodb

%prep
%autosetup -n %{pypi_name}-%{version}
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
%if %{without redis}
# If we don’t have a new enough redis, we won’t need the extra fixtures for it:
sed -r -i 's/^import redis/# &/' tests/conftest.py
%endif
# Allow newer versions of doc dependencies.
#
# Drop unused “furo” HTML theme.
#
# Missing dependencies (but we can build documentation anyway):
# - python3dist(sphinx-paramlinks)
sed -r -e 's/==/>=/' \
    -e '/^[[:blank:]]*(furo|sphinx-paramlinks)/d' \
    requirements/docs.txt |
%if 0%{?fc36}
    # Tolerate Sphinx 4 in addition to the Sphinx 5 desired by upstream.
    sed -r -e 's/(Sphinx[>=]=)5/\14/' |
%endif
%if 0%{?fc36} || 0%{?fc37}
    # Tolerate versions of sphinxext-opengraph older than upstream wants
    sed -r -e 's/(sphinxext-opengraph)([>=]=.*)/\1/' |
%endif
  tee requirements/docs-filtered.txt
sed -r -i '/(paramlinks)/d' doc/source/conf.py
# Cannot use remote intersphinx inventories in offline build:
echo 'intersphinx_mapping.clear()' >> doc/source/conf.py

# Relax packaging version constraint
sed -i 's/packaging>=21,<23/packaging>=21,<24/' requirements/main.txt

%generate_buildrequires
%if %{with async_redis} && %{with async_memcached} && %{with async_mongodb} && %{with redis}
%pyproject_buildrequires -x all %{?with_tests:requirements/test-filtered.txt}
%else
%{pyproject_buildrequires \
  %{?with_tests:requirements/test-filtered.txt} \
  %{?with_doc_pdf:requirements/docs-filtered.txt} \
  %{?with_async_redis:-x async-redis} \
  %{?with_async_memcached:-x async-memcached} \
  %{?with_async_mongodb:-x async-mongodb} \
  %{?with_redis:-x redis -x rediscluster} \
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
%if %{without redis}
# We cannot import these at all:
ignore="${ignore-} --ignore=tests/storage/test_redis.py"
ignore="${ignore-} --ignore=tests/storage/test_redis_cluster.py"
ignore="${ignore-} --ignore=tests/storage/test_redis_sentinel.py"
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
%autochangelog
