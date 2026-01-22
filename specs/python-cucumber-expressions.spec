Name:           python-cucumber-expressions
Version:        18.1.0
Release:        %autorelease
Summary:        Cucumber Expressions - a simpler alternative to Regular Expressions

License:        MIT
URL:            https://github.com/cucumber/cucumber-expressions
# The GitHub archive has test data files; the PyPI sdist does not.
Source:         %{url}/archive/v%{version}/cucumber-expressions-%{version}.tar.gz

# Downstream-only: remove the upper bound on the version of uv_build
# We must work with what is packaged; multiple compat versions are not planned.
Patch:          0001-Downstream-only-remove-the-upper-bound-on-the-versio.patch

BuildSystem:            pyproject
BuildOption(install):   -l cucumber_expressions

BuildArch:      noarch

# Python test dependencies; see the dev dependency group defined in
# python/pyproject.toml. Not all from that group are actually needed, so we
# list these manually.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist PyYAML}

%global common_description %{expand:
Cucumber Expressions is an alternative to Regular Expressions with a more
intuitive syntax.}

%description %{common_description}


%package -n python3-cucumber-expressions
Summary:        %{summary}

%description -n python3-cucumber-expressions %{common_description}


%generate_buildrequires -p
cd python


%build -p
cd python


%install -p
install -t '%{buildroot}%{_pkgdocdir}/general' -p -m 0644 -D \
    ARCHITECTURE.md CHANGELOG.md README.md
install -t '%{buildroot}%{_pkgdocdir}' -p -m 0644 -D python/README.md


%check -a
%pytest python/tests -v


%files -n python3-cucumber-expressions -f %{pyproject_files}
%doc %{_pkgdocdir}/


%changelog
%autochangelog
