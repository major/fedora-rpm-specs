Name:           python-helpdev
Version:        0.7.1
Release:        %autorelease
Summary:        HelpDev – Extracts information about the Python environment easily

# The GitLab archive contains tests and documentation; the PyPI sdist doesn’t.
%global forgeurl https://gitlab.com/dpizetta/helpdev
%global tag v%{version}
%forgemeta

# The entire source is MIT, except for “Images,” which are CC-BY-4.0 (an
# allowed license for content). The images in question seem to be only the
# contents of docs/images/, which are not included in the binary RPMs (since we
# stopped shipping Sphinx-generated documentation).
License:        MIT
SourceLicense:  %{license} AND CC-BY-4.0
URL:            %{forgeurl}
Source:         %{forgesource}

# Remove useless shebang lines from package modules
# https://gitlab.com/dpizetta/helpdev/-/merge_requests/4
Patch:          %{forgeurl}/-/merge_requests/4.patch

BuildSystem:    pyproject
BuildOption(generate_buildrequires): --extras memory_info
BuildOption(install): --assert-license helpdev

BuildArch:      noarch

# Selected test dependencies from req-test.txt; most entries in that file are
# for linters, code coverage, etc. Note that we use pytest directly because tox
# doesn’t add anything useful for us in this package.
BuildRequires:  %{py3_dist pytest}

# The generated man page is pretty good in this case; it’s probably not worth
# hand-writing one.
BuildRequires:  help2man

%global common_description %{expand:
Helping users and developers to get information about the environment to report
bugs or even test your system without spending a day on it. It can get
information about hardware, OS, paths, Python distribution and packages,
including Qt-things.}

%description %{common_description}


%package -n python3-helpdev
Summary:        %{summary}

Recommends:     python3-helpdev+memory_info = %{version}-%{release}

# PDF docs and separate -doc subpackage were dropped in F45; we need the
# upgrade path through F47.
Obsoletes:      python-helpdev-doc < 0.7.1-23

%description -n python3-helpdev %{common_description}


%pyproject_extras_subpkg -n python3-helpdev memory_info


%install -a
# Generating the man page in %%install allows us to use the installed entry
# point; horrible hacks would be required to do this in %%build.
install --directory '%{buildroot}%{_mandir}/man1'
%{py3_test_envvars} help2man --no-info \
    --output='%{buildroot}%{_mandir}/man1/helpdev.1' helpdev


%check -a
%pytest --verbose


%files -n python3-helpdev -f %{pyproject_files}
%doc CHANGES.rst
%doc README.rst
# Text files, mostly sample output
%doc examples/

%{_bindir}/helpdev
%{_mandir}/man1/helpdev.1*


%changelog
%autochangelog
