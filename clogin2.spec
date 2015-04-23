Name: 		clogin2         
Version: 	2.0rc5
Release:        0
Summary: 	multi-vendor login tool, forked from RANCID

Group:          Applications/Internet
License:        BSD
URL:            https://github.com/dwcarder/clogin2
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: 	noarch

Requires:       expect openssh openssh-clients tcl-syslog
Conflicts:	rancid

%description
%{summary}
%define  debug_package %{nil}

%prep
%setup -q

%build
# Empty section

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/ns/bin
mkdir -p %{buildroot}/usr/local/ns/share/clogin2/doc
cp clogin2 %{buildroot}/usr/local/ns/bin
cp cleanSshKnownHosts.pl %{buildroot}/usr/local/ns/bin
cp cloginrc %{buildroot}/usr/local/ns/share/clogin2/doc
cp LICENSE %{buildroot}/usr/local/ns/share/clogin2/doc

%clean
rm -rf %{buildroot}

%post
ln -f -s /usr/local/ns/bin/clogin2 /usr/local/ns/bin/clogin

%files
%defattr(755,root,root,-)
/usr/local/ns/bin/clogin2
/usr/local/ns/bin/cleanSshKnownHosts.pl
%defattr(644,root,root,-)
/usr/local/ns/share/clogin2/doc/cloginrc
/usr/local/ns/share/clogin2/doc/LICENSE


%changelog
*Wed Apr 22 2015 <mtinberg@wisc.edu> 2.0rc4-0
- fix git tags

*Wed Apr 22 2015 <mtinberg@wisc.edu> 2.0rc3-0
- incorporate ssh key mangement utility when hostkey changes

*Thu Mar 26 2015 <dwcarder@wisc.edu> 2.0-0 
--Fix specfile buildroo, incorporate last patches made in RCS since Jul 9 2014

*Wed Jul 9 2014 <dwcarder@wisc.edu> 1.1-1 
--Fixes to tcl-syslog

*Wed Jul 3 2014 <dwcarder@wisc.edu> 1.0-1 
--Initial Packaging Build.

