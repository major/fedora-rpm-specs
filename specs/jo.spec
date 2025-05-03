Name:           jo
Summary:        Small utility to create JSON objects
Version:        1.9
Release:        %autorelease

URL:            https://github.com/jpmens/jo
Source:         %{url}/archive/%{version}/jo-%{version}.tar.gz
# The entire source is GPL-2.0-or-later, except:
#
#   - json.c and json.h are MIT
#   - base64.c and base64.h are LicenseRef-Fedora-Public-Domain; text
#     added to public-domain-text.txt in fedora-license-data:
#     https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/206
License:        GPL-2.0-or-later AND MIT AND LicenseRef-Fedora-Public-Domain

# Update GPL-2.0-or-later license notices
# https://github.com/jpmens/jo/pull/216
# Merged upstream, so we are comfortable patching downstream.
Patch:          %{url}/pull/216.patch

# Add a copy of the GPLv2 license text
# https://github.com/jpmens/jo/pull/217
Patch:          %{url}/pull/217.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  meson
# No pandoc on EPEL10 yet:
%if !0%{?el10}
# Rebuild jo.1 and jo.md; we can omit this if it ever breaks.
BuildRequires:  pandoc
%endif

# For automatic installation of completions support via meson
BuildRequires:  pkgconfig(bash-completion)

# Upstream URL: http://ccodearchive.net/info/json.html
# Upstream VCS: https://github.com/rustyrussell/ccan/tree/master/ccan/json
#
# This is a copylib and not designed to be built as a separate library. See
# https://fedoraproject.org/wiki/Bundled_Libraries_Virtual_Provides; even under
# the old guidelines, in which bundled libraries required FPC exemptions, a
# variety of similar CCAN modules had exemptions as copylibs.
#
# Inspection of https://github.com/rustyrussell/ccan/tree/master/ccan/json
# shows the bundled code is consistent with version 0.1 (as declared in a
# comment in https://github.com/rustyrussell/ccan/blob/master/ccan/json/_info),
# but has been forked with various small modifications in json.c.
Provides:       bundled(ccan-json) = 0.1

# The public-domain base64 implementation looks like a copylib, but I could not
# find the upstream from which it was copied, so I am not treating it as a
# bundled dependency.

%description
This is jo, a small utility to create JSON objects

  $ jo -p name=jo n=17 parser=false
  {
      "name": "jo",
      "n": 17,
      "parser": false
  }

or arrays

  $ seq 1 10 | jo -a
  [1,2,3,4,5,6,7,8,9,10]


%prep
%autosetup -p1


%conf
%meson


%build
%meson_build


%install
%meson_install
# Upstream’s Autotools build system installs the zsh completions, but the meson
# version does not; we can handle it manually.
install -D -p -m 0644 jo.zsh '%{buildroot}%{zsh_completions_dir}/_jo'


%check
ln -s '%{buildroot}%{_bindir}/jo' .
bash -e ./tests/jo.test


%files
%license COPYING
%license LICENSE.GPLv2
%doc AUTHORS
%doc ChangeLog
# NEWS not included because it is empty
%doc press.md
%doc README.md
%doc jo.md

%{_bindir}/jo
%{_mandir}/man1/jo.1*

%{bash_completions_dir}/jo.bash
%{zsh_completions_dir}/_jo


%changelog
%autochangelog
