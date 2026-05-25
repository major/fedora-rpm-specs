Name:           python-cucumber-expressions
Version:        19.0.1
Release:        %autorelease
Summary:        Cucumber Expressions - a simpler alternative to Regular Expressions

License:        MIT
URL:            https://github.com/cucumber/cucumber-expressions
# The GitHub archive has test data files; the PyPI sdist does not.
Source:         %{url}/archive/v%{version}/cucumber-expressions-%{version}.tar.gz

BuildSystem:    pyproject
BuildOption(generate_buildrequires): --directory python
BuildOption(build): --directory python
BuildOption(install): --assert-license cucumber_expressions

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


%prep -a
# Downstream-only: remove the upper bound on the version of uv_build
# We must work with what is packaged; multiple compat versions are not planned.
%pyproject_patch_dependency uv_build:drop_upper


%install -p
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_pkgdocdir}/general' \
    ARCHITECTURE.md CHANGELOG.md README.md
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_pkgdocdir}' python/README.md


%check -a
%pytest python/tests --verbose


%files -n python3-cucumber-expressions -f %{pyproject_files}
%doc %{_pkgdocdir}/


%changelog
%autochangelog
