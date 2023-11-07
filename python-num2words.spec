# Currently disabled because the BR isn't available in Fedora
%bcond_with tests

%global forgeurl https://github.com/savoirfairelinux/num2words

%global _description %{expand:
Convert numbers to words in multiple languages, it is a library that converts
numbers like ``42`` to words like ``forty-two``.  It supports multiple
languages (English, French, Spanish, German and Lithuanian) and can even
generate ordinal numbers like ``forty-second``.}

Name:           python-num2words
Version:        0.5.13
Release:        %autorelease
Summary:        Module to convert numbers to words

%forgemeta

# spdx
License:        LGPL-2.0-or-later
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  help2man

%description %_description

%package -n python3-num2words
Summary:        %{summary}

%if %{with tests}
BuildRequires:  %{py3_dist delegator.py}
%endif

%description -n python3-num2words %_description

%prep
%forgesetup
# Remove bundled egg-info
rm -rf num2words.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files num2words

# generate man pages
for binary in "num2words"
do
    echo "Generating man page for ${binary// /-/}"
    PYTHONPATH="$PYTHONPATH:%{buildroot}/%{python3_sitelib}/" PATH="$PATH:%{buildroot}/%{_bindir}/" help2man --no-info --no-discard-stderr --name="${binary}" --version-string="${binary} %{version}" --output="${binary// /-}.1" "${binary}"
    cat "${binary// /-}.1"
    install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D "${binary// /-}.1"
done

%check
%pyproject_check_import
%if %{with tests}
%{__python3} setup.py test
%endif

%files -n python3-num2words -f %{pyproject_files}
%doc README.rst
%{_bindir}/num2words
%{_mandir}/man1/num2words.*

%changelog
%autochangelog
