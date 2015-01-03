#
# spec file for package infobash
#
# Copyright (C) 2005-2015 Stefan Lippers-Hollmann <s.l-h@gmx.de>
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Upstream location:
# http://svn.berlios.de/svnroot/repos/fullstory/infobash/trunk/
#

# norootforbuild
# neededforbuild

BuildRequires: cpio diffutils file gzip make man mktemp patch tar

Name:         infobash
URL:          http://svn.berlios.de/svnroot/repos/fullstory/infobash/trunk/
License:      GPL
Group:        System/Packages
Provides:     infobash
Requires:     bash, coreutils, net-tools, procps, pciutils, grep, gawk
Autoreqprov:  on
Version:      3.48
Release:      1
Summary:      System info script for irc
Source:       infobash_%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch

%description
Infobash is a system information script for IRC (Internet Relay Chat) clients.
A system information script can display all kinds of things about your
hardware and software to users in a chatroom,  so they can help you diagnose
problems, ... or just marvel at your system specs and kernel version ;)
It was created to serve the need for a infoscript that isn't dependant on a
particular irc client. Because most irc clients support the /exec command, a
script that runs with /exec would be most portable.



Authors:
--------
    M.L. de Boer <ltown2@web.de>

%prep
%setup
#gzip -d -c infobash_%{version}.tar.gz | tar xf -

%build

%install
# Prepare build root
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT

##
# infobash stuff
##
# prepare directory structure, copy files

install -d -m 0755 $RPM_BUILD_ROOT/etc
install -d -m 0755 $RPM_BUILD_ROOT/usr
install -d -m 0755 $RPM_BUILD_ROOT/usr/bin

#copy files
install -m 0755 infobash $RPM_BUILD_ROOT/usr/bin/infobash
install -m 0644 infobash.conf $RPM_BUILD_ROOT/etc/

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
/etc/*
/usr/bin/*

%changelog -n infobash
* Sun Feb 27 2010 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- adapt to aptosid - 3.35
- collate core info for multi-core CPUs.
* Thu Aug 26 2010 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- adapt to aptosid - 3.34
* Mon Apr 26 2010 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- updated to current version, use nicinfo if available - 3.31
* Sat Feb 6 2010 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- updated to current version, use nicinfo if available - 3.29
* Mon Jan 18 2010 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- updated to current version, fix spelling - 3.28
* Mon Jan 18 2010 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- updated to current version, fix spelling - 3.27
* Mon Jan 18 2010 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- updated to current version - 3.26
* Sun Nov 09 2008 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- updated to current version - 3.03
* Thu Jul 18 2005 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- updated to current version - 2.01
* Thu Jul 17 2005 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- updated to current version - 2.00b21
* Thu Jul 14 2005 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- updated to current version - 2.00b20
* Tue Mar 08 2005 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- updated to current version - version 2.00b15
* Sun Oct 10 2004 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- package created - version 2.00b11
