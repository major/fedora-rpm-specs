%bcond_without check
# Some tests use a package that uses this.
%bcond_with bootstrap

# The output from a standard Hugo package build can be overwhelming when
# trying to diagnose package build errors. A less verbose follow up
# is:
#
# 1. Run "rpmbuild -ba hugo.spec >/tmp/LOG 2>&1" to capture all of
# the output.
#
# 2. Look for the command "go build ..." in that output.
#
# 3. Enter the BUILD/hugo-VERSION directory.
#
# 4. Export the two variables set before "go build ...".
#
# 5. Run the "go build ..." command, but without the "-v" and "-x".

# https://github.com/gohugoio/hugo
%global goipath github.com/gohugoio/hugo
Version:        0.111.3

%gometa -f

%global common_description %{expand:
Hugo is a static HTML and CSS website generator written in Go. It is optimized
for speed, easy use and configurability. Hugo takes a directory with content
and templates and renders them into a full HTML website.}

%global golicenses      LICENSE docs/LICENSE.md docs/themes/gohugoioTheme/license.md
%global godocs          docs examples README.md CONTRIBUTING.md

Name:           hugo
Release:        %autorelease
Summary:        The world’s fastest framework for building websites

# Upstream license specification: Apache-2.0 and MIT
License:        ASL 2.0 and MIT
URL:            %{gourl}
Source0:        %{gosource}
# Skip tests that uses the network.
# Based on https://sources.debian.org/data/main/h/hugo/0.58.3-1/debian/patches/0005-skip-modules-TestClient.patch
Patch0001:      0010-skip-modules-TestClient.patch
# Use clbanning-mxj, not clbanning-mxj-v2
# See https://github.com/gohugoio/hugo/issues/9860
Patch0002:      0020-clbanning-mxj.patch
# Use nicksnyder-go-i18n, not gohugoio/go-i18n/
# See https://github.com/gohugoio/hugo/issues/9860
# and https://github.com/nicksnyder/go-i18n/pull/253
Patch0003:      0030-nicksnyder-go-i18n.patch

BuildRequires:  golang(github.com/bep/golibsass/libsass) >= 0.7.0

# This is in response to Red Hat Bugzilla #2104346. The full dependencies
# for Hugo are large, including GCC and the Go toolchain. For example,
# "hugo server" will not work without these. It might be beneficial to avoid
# such large dependencies in some instances---such as CI pipelines---that
# do not require "hugo server". Thus golang-bin is a weak dependency.
#
# Also see the discussion at https://src.fedoraproject.org/rpms/hugo/pull-request/13.
Recommends:     golang-bin

%description
%{common_description}

%gopkg

%prep
%goprep

%autopatch -p1

# Replace blackfriday import path to avoid conflict with v2
sed -i \
    -e 's|"github.com/russross/blackfriday|"gopkg.in/russross/blackfriday.v1|' \
    $(find . -name '*.go')

# Pin github.com/evanw/esbuild to v0.8.20
# See https://github.com/gohugoio/hugo/issues/8141
sed -i \
    -e 's|"github.com/evanw/esbuild|"github.com/evanw/esbuild-0.8.20|' \
    $(find . -name '*.go')

# Skip test that assumes directory is in a git repository
sed -i '/TestPageWithLastmodFromGitInfo/a t.Skip()' hugolib/page_test.go

%if %{with bootstrap}
# Delete test using github.com/gohugoio/testmodBuilder/mods which has a
# dependency loop.
rm hugolib/hugo_modules_test.go
%endif

%generate_buildrequires
%go_generate_buildrequires

%build
BUILDTAGS=extended LDFLAGS="${LDFLAGS} -X %{goipath}/common/hugo.buildDate=$(date --iso=seconds --date=@$SOURCE_DATE_EPOCH) -X %{goipath}/common/hugo.vendorInfo=Fedora:%{version}-%{release}" %gobuild -o %{gobuilddir}/bin/hugo %{goipath}
%{gobuilddir}/bin/hugo gen autocomplete >hugo-completion
%{gobuilddir}/bin/hugo gen man

%install
%gopkginstall

install -d -p %{buildroot}%{_bindir}
install -Dp -m 0755 %{gobuilddir}/bin/hugo %{buildroot}%{_bindir}
install -Dp hugo-completion %{buildroot}%{_datadir}/bash-completion/completions/hugo
install -Dp man/* -t %{buildroot}%{_mandir}/man1

%if %{with check}
%check
# langs/i18n: Patched gohugoio/go-i18n/ back to nicksnyder/go-i18n.
# resources/resource_factories/create: Now fails with latest Rawhide dependencies.
# resources/resource_transformers/js: Error message formats have changed.
# tpl/internal/go_templates/htmltemplate: Now fails with latest Rawhide dependencies.
# tpl/internal/go_templates/texttemplate: Now fails with latest Rawhide dependencies.
%gocheck -d langs/i18n -d resources/resource_factories/create -d resources/resource_transformers/js -d tpl/internal/go_templates/htmltemplate -d tpl/internal/go_templates/texttemplate
%endif

%files
%doc CONTRIBUTING.md README.md docs
%license LICENSE
%{_bindir}/hugo
%{_datadir}/bash-completion/completions/hugo
%{_mandir}/man1/*.1*

%gopkgfiles

%changelog
%autochangelog
