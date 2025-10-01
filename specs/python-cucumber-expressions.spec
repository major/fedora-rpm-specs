Name:           python-cucumber-expressions
Version:        18.0.1
Release:        %autorelease
Summary:        Cucumber Expressions - a simpler alternative to Regular Expressions

License:        MIT
URL:            https://github.com/cucumber/cucumber-expressions
# The GitHub archive has test data files; the PyPI sdist does not.
Source:         %{url}/archive/v%{version}/cucumber-expressions-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -L cucumber_expressions

BuildArch:      noarch

# Python test dependencies; see [tool.poetry.dev-dependencies] in
# python/pyproject.toml. Not all from that section are actually needed, so we
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
%license python/LICENSE
%doc %{_pkgdocdir}/


%changelog
%autochangelog
