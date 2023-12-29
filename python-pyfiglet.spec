%global pypi_name   pyfiglet

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        %autorelease
Summary:        Pure-python FIGlet implementation

# The following fonts are under another licence, the rest of the code is MIT.
#
# BSD:
# - banner.flf
# - big.flf
# - block.flf
# - bubble.flf
# - digital.flf
# - ivrit.flf
# - lean.flf
# - mini.flf
# - mnemonic.flf
# - script.flf
# - shadow.flf
# - slant.flf
# - small.flf
# - smscript.flf
# - smshadow.flf
# - smslant.flf
# - standard.flf
# - term.flf
#
# NTP:
# - clb6x10.flf
# - clb8x10.flf
# - clb8x8.flf
# - cli8x8.flf
# - clr4x6.flf
# - clr5x10.flf
# - clr5x6.flf
# - clr5x8.flf
# - clr6x10.flf
# - clr6x6.flf
# - clr6x8.flf
# - clr7x10.flf
# - clr7x8.flf
# - clr8x10.flf
# - clr8x8.flf
# - cour.flf
# - courb.flf
# - courbi.flf
# - couri.flf
# - helv.flf
# - helvb.flf
# - helvbi.flf
# - helvi.flf
# - sbook.flf
# - sbookb.flf
# - sbookbi.flf
# - sbooki.flf
# - times.flf
# - xcour.flf
# - xcourb.flf
# - xcourbi.flf
# - xcouri.flf
# - xhelv.flf
# - xhelvb.flf
# - xhelvbi.flf
# - xhelvi.flf
# - xsbook.flf
# - xsbookb.flf
# - xsbookbi.flf
# - xsbooki.flf
# - xtimes.flf
#
# HPND:
# - 5x8.flf
# - chartr.flf
# - chartri.flf
# - xchartr.flf
# - xchartri.flf
#
# X11:
# - 5x7.flf
# - 6x9.flf
License:        MIT AND BSD-3-Clause AND NTP AND HPND AND X11
URL:            https://github.com/pwaller/pyfiglet
Source0:        pyfiglet-%{version}-no-contrib-font.tar.gz
# Removes all fonts in pyfiglet/fonts-contrib
# USAGE:
#   ./generate-pyfiglet-tarball.sh VERSION
Source1:        generate-pyfiglet-tarball.sh

# https://github.com/pwaller/pyfiglet/pull/137
Patch0:         0001-Use-slant-instead-of-doh-to-use-only-fonts-contrib.patch

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  git-core
BuildRequires:  glibc-common
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)


%global _description %{expand:
pyfiglet is a full port of FIGlet (http://www.figlet.org/) into pure python. It
takes ASCII text and renders it in ASCII art fonts (like the title above, which
is the 'block' font).}

%description %{_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{version} -S git

mv pyfiglet/fonts-standard pyfiglet/fonts

# Resolve RPMLint errors
%py3_shebang_fix pyfiglet/{__init__,test}.py

# Change figfont.txt encoding
iconv -f ISO8859-1 -t UTF-8 doc/figfont.txt -o figfont.txt

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{pypi_name}

chmod 0755 %{buildroot}%{python3_sitelib}/%{pypi_name}/{__init__,test}.py
install -Dpm 0644 -t %{buildroot}%{_mandir}/man1/ doc/%{pypi_name}.1


%check
%pytest

rm %{buildroot}%{python3_sitelib}/%{pypi_name}/fonts/TEST_ONLY.flf


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md figfont.txt
%{_bindir}/%{pypi_name}
%{_mandir}/man1/%{pypi_name}.1.*


%changelog
%autochangelog
