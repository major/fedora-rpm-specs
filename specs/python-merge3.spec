Name:           python-merge3
Version:        0.0.16
Release:        %autorelease
Summary:        Python implementation of 3-way merge

License:        GPL-2.0-or-later
URL:            https://github.com/breezy-team/merge3
Source0:        %{url}/archive/v%{version}/merge3-%{version}.tar.gz
# Man page hand-written for Fedora in groff_man(7) format based on --help text
# and on README.rst.
Source1:        merge3.1

# tox: allow passing positional arguments through to unittest
# https://github.com/breezy-team/merge3/pull/130
Patch:          %{url}/pull/130.patch

BuildSystem:    pyproject
BuildOption(generate_buildrequires): --tox
BuildOption(install): --assert-license merge3

BuildArch:      noarch

%global common_description %{expand:
A Python implementation of 3-way merge of texts.

Given BASE, OTHER, THIS, tries to produce a combined text incorporating the
changes from both BASE->OTHER and BASE->THIS. All three will typically be
sequences of lines.}

%description %{common_description}


%package -n python3-merge3
Summary:        %{summary}

%description -n python3-merge3 %{common_description}


%install -a
install -D --target='%{buildroot}%{_mandir}/man1' \
    --preserve-timestamps --mode=0644 '%{SOURCE1}'


%check -a
%tox -- -- --verbose


%files -n python3-merge3 -f %{pyproject_files}
%doc README.rst

%{_bindir}/merge3
%{_mandir}/man1/merge3.1*


%changelog
%autochangelog
