# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

%if 0%{?el9}
# https://bugzilla.redhat.com/show_bug.cgi?id=2034654
%bcond_with gevent
%else
%bcond_without gevent
%endif

Summary:        OpenTracing interface for Python
Name:           python-opentracing
Version:        2.4.0
Release:        7%{?dist}

# The files are under the Apache License 2.0,
# except for:
# - mocktracer-related files
# - scope-related files
# - tests/conftest.py
# which are under the Expat License (classified as MIT by the Open
# Source Initiative).
License:        ASL 2.0 and MIT
URL:            https://github.com/opentracing/opentracing-python
Source0:        %{url}/archive/%{version}/opentracing-python-%{version}.tar.gz

# Issue filed upstream as https://github.com/opentracing/opentracing-python/issues/142
# Upstream has merged the change on master as https://github.com/opentracing/opentracing-python/pull/143
Patch0:         0001-Do-not-use-mock-the-PyPI-backport-library-when-possi.patch
# Replace @asyncio.coroutine with “async def” for Python 3.11
# https://github.com/opentracing/opentracing-python/pull/159
Patch1:         %{url}/pull/159.patch

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  make
BuildRequires:  texinfo
%if %{with doc_pdf}
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
# Required to provide its intersphinx inventory
%if ! 0%{?el9}
BuildRequires:  python3-docs
%endif
%endif

%global _description %{expand:
This library is a Python platform API for OpenTracing.

It allows Python programs to interact with an OpenTracing server.}

%description
%{_description}

%prep
%autosetup -n opentracing-python-%{version} -p1
%if 0%{?el9}
echo 'intersphinx_mapping.clear()' >> docs/conf.py
%else
# Reconfigure intersphinx to use the local inventory.
sed -e '/^ \+.python.:/s,None,"%{_docdir}/python3-docs/html/objects.inv",' -i docs/conf.py
%endif
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/\b(pytest-cov|flake8(-quotest)?)\b/d' setup.py
# https://pypi.org/project/doubles/ is not yet packaged, and does not seem to
# be used in practice.
sed -r -i '/\bdoubles\b/d' setup.py
%if %{without gevent}
# https://bugzilla.redhat.com/show_bug.cgi?id=2034654
sed -r -i '/\bgevent\b/d' setup.py
%endif

%generate_buildrequires
%pyproject_buildrequires -x tests

%build
%pyproject_wheel

# Generate the documentation.
for target in info %{?with_doc_pdf:latex}
do
  PYTHONPATH="%{pyproject_build_lib}" \
      %make_build -C docs "${target}" SPHINXOPTS='%{?_smp_mflags}'
done
%if %{with doc_pdf}
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files opentracing
mkdir -p %{buildroot}%{_infodir}
cp -p docs/_build/texinfo/opentracing-python.info %{buildroot}%{_infodir}/

%check
# Based on the “test” Makefile target, but with coverage options removed
%pytest \
%if %{without gevent}
    --ignore='tests/scope_managers/test_gevent.py' \
%endif
    --tb short -rxs opentracing tests

%package -n python3-opentracing
Summary: %{summary}

%description -n python3-opentracing
%{_description}

%files -n python3-opentracing -f %{pyproject_files}
# pyproject_files handles LICENSE; verify with “rpm -qL -p …”
%doc README.rst
%doc CHANGELOG.rst
%{_infodir}/opentracing-python.info*

%package doc
Summary: %{summary} - documentation

%description doc
%{_description}

This package contains the documentation.

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/opentracing-python.pdf
%endif

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 2.4.0-6
- Fix Python 3.11 compatibility

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.4.0-5
- Rebuilt for Python 3.11

* Fri Apr 22 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 2.4.0-4
- Assorted minor spec file cleanup
- Build Sphinx-generated documentation as PDF instead of HTML
- Switch to pyproject-rpm-macros (“new Python guidelines”)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Dec 10 2020 Fabrice BAUZAC <noon@mykolab.com> 2.4.0-1
- Initial version.
