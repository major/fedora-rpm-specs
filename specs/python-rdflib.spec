%global srcname rdflib

%bcond docs 0
%bcond tests 0
%if 0%{?fedora}
%bcond docs 1
%bcond tests 1
%endif

Name:           python-%{srcname}
Version:        7.1.3
Release:        %autorelease
Summary:        Python library for working with RDF
License:        BSD-3-Clause
URL:            https://github.com/RDFLib/rdflib
BuildArch:      noarch

Source:         %{pypi_source}

BuildRequires:  python%{python3_pkgversion}-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif
%if %{with docs}
BuildRequires:  python3dist(myst-parser)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-autodoc-typehints)
BuildRequires:  python3dist(sphinxcontrib-apidoc)
BuildRequires:  python3dist(typing-extensions)
%endif

%description
RDFLib is a pure Python package for working with RDF. RDFLib contains most
things you need to work with RDF, including parsers and serializers for
RDF/XML, N3, NTriples, N-Quads, Turtle, TriX, Trig and JSON-LD, a Graph
interface which can be backed by any one of a number of Store implementations,
store implementations for in-memory, persistent on disk (Berkeley DB) and
remote SPARQL endpoints, a SPARQL 1.1 implementation - supporting SPARQL 1.1
Queries and Update statements - and SPARQL function extension mechanisms.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname}
RDFLib is a pure Python package for working with RDF. RDFLib contains most
things you need to work with RDF, including parsers and serializers for
RDF/XML, N3, NTriples, N-Quads, Turtle, TriX, Trig and JSON-LD, a Graph
interface which can be backed by any one of a number of Store implementations,
store implementations for in-memory, persistent on disk (Berkeley DB) and
remote SPARQL endpoints, a SPARQL 1.1 implementation - supporting SPARQL 1.1
Queries and Update statements - and SPARQL function extension mechanisms.

%if %{with docs}
%package -n python%{python3_pkgversion}-%{srcname}-docs
Summary:        Documentation for %{srcname}

%description -n python%{python3_pkgversion}-%{srcname}-docs
Documentation for %{srcname}, a Python library for working with RDF.
%endif

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Various .py files within site-packages have a shebang line but aren't
# flagged as executable.
# I've gone through them and either removed the shebang or made them
# executable as appropriate:

# __main__ parses URI as N-Triples:
chmod +x %{buildroot}%{python3_sitelib}/rdflib/plugins/parsers/ntriples.py

# __main__ parses the file or URI given on the command line:
chmod +x %{buildroot}%{python3_sitelib}/rdflib/tools/rdfpipe.py

# __main__ runs a test (well, it's something)
chmod +x %{buildroot}%{python3_sitelib}/rdflib/extras/external_graph_libs.py

# sed these headers out as they include no __main__
for lib in %{buildroot}%{python3_sitelib}/rdflib/extras/describer.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

# sed shebangs
sed -i '1s=^#!/usr/bin/\(python\|env python\).*=#!%{__python3}='  \
    %{buildroot}%{python3_sitelib}/rdflib/extras/infixowl.py \
    %{buildroot}%{python3_sitelib}/rdflib/extras/external_graph_libs.py \
    %{buildroot}%{python3_sitelib}/rdflib/plugins/parsers/ntriples.py \
    %{buildroot}%{python3_sitelib}/rdflib/tools/rdfpipe.py \
    %{buildroot}%{python3_sitelib}/rdflib/plugins/parsers/notation3.py

%if %{with docs}
# generate html docs
PYTHONPATH=%{buildroot}%{python3_sitelib} sphinx-build-3 -b html -d docs/_build/doctree docs docs/_build/html
# remove the sphinx-build-3 leftovers
rm -rf docs/_build/html/.{doctrees,buildinfo}
%endif

%pyproject_save_files -L %{srcname}

%if %{with tests}
%check
%pytest -k "not rdflib and not rdflib.extras.infixowl and not \
            test_example and not test_suite and not \
            test_infix_owl_example1 and not test_context and not \
            test_service and not test_simple_not_null and not \
            test_sparqleval and not test_parser \
%if "%{version}" == "7.0.0" && (! 0%{?fedora} || 0%{?fedora} >= 42)
            and not test_literal_addsub[2006-07-01T20:52:00-P123D-aplusb-2006-11-01T12:50:00] \
            and not test_literal_addsub[2006-07-01T20:52:00-2006-11-01T12:50:00-bminusa-P123D] \
%endif
            " -m "not webtest"
%endif

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/csv2rdf
%{_bindir}/rdf2dot
%{_bindir}/rdfgraphisomorphism
%{_bindir}/rdfpipe
%{_bindir}/rdfs2dot

%if %{with docs}
%files -n python%{python3_pkgversion}-%{srcname}-docs
%license LICENSE
%doc docs/_build/html
%endif

%changelog
%autochangelog
